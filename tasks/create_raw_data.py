import json
from genson import SchemaBuilder
from hypergol import Task
from hypergol.name_string import NameString
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData

class PSchemaBuilder:

    def __init__(self, schema=None):
        self.builder = SchemaBuilder()
        if schema is not None:
            self.builder.add_schema(schema)

    def __reduce_ex__(self, protocol):
        return self.__class__, (self.to_schema(), )

    def add_schema(self, schema):
        self.builder.add_schema(schema)

    def add_object(self, data):
        self.builder.add_object(data)

    def to_schema(self):
        return self.builder.to_schema()


def get_hypergol_commands(name, properties, plurals):
    def get_class_name(name):
        if name[-1] == 's' and name not in plurals:
            raise ValueError(f'{name} not in plurals')
        return NameString(plurals.get(name,name))
            
    className = get_class_name(name)
    propertiesString = ''
    for propertyName, propertySchema in properties.items():
        if propertySchema['type'] == 'object':
            propertyClassName = get_hypergol_commands(
                name=propertyName,
                properties=propertySchema['properties'],
                plurals=plurals
            )
            propertiesString += f' {propertyName}:{propertyClassName}'
        elif propertySchema['type'] == 'array':
            if propertySchema['items']['type'] == 'object':
                itemClassName = get_hypergol_commands(
                    name=propertyName,
                    properties=propertySchema['items']['properties'],
                    plurals=plurals
                )
            elif isinstance(propertySchema['items'], list):
                itemClassName = next(v for v in propertySchema['items']['type'] if v !='null')
            else:
                itemClassName = propertySchema['items']['type']
            propertiesString += f' "{propertyName}:List[{itemClassName}]"'
        elif isinstance(propertySchema['type'], list):
            nullableType = next(v for v in propertySchema['type'] if v !='null')
            propertiesString += f' "{propertyName}:List[{nullableType}]"'
        else:
            propertiesString += f' {propertyName}:{propertySchema["type"]}'
    print(f'python -m hypergol.cli.create_data_model {className}{propertiesString} --force')
    return className

def _dict_to_list(k, v, name):
    v[name] = k
    return v

class CreateRawData(Task):

    def __init__(self, rawDataLocation, plurals, *args, **kwargs):
        super(CreateRawData, self).__init__(*args, **kwargs)
        self.rawDataLocation = rawDataLocation
        self.plurals = plurals

    def init(self):
        self.results['builder'] = PSchemaBuilder()
        self.results['builder'].add_schema({"type": "object", "properties": {}})

    def run(self, rawMetadata):
        filenames = [filename.strip() for filename in rawMetadata.pdfJsonFiles.split(';')]
        rawData =  RawData(
            cordUid=rawMetadata.cordUid,
            data=[],
            rawMetadata=rawMetadata
        )
        for filename in filenames:
            data=json.load(open(f'{self.rawDataLocation}/{filename}','rt'))
            data['bib_entries']=[_dict_to_list(k,v,'bib_entry_id') for k, v in data['bib_entries'].items()]
            data['ref_entries']=[_dict_to_list(k,v,'ref_entry_id') for k, v in data['ref_entries'].items()]
            rawData.data.append(json.dumps(data))
            self.results['builder'].add_object(data)
        self.output.append(rawData)

    def finish(self, jobReports, threads):
        builder = PSchemaBuilder()
        for jobReport in jobReports:
            builder.add_schema(jobReport.results['builder'])
        get_hypergol_commands(
            name='article',
            properties=builder.to_schema()['properties'],
            plurals=self.plurals
        )