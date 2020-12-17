import fire
from hypergol import HypergolProject
from hypergol import Pipeline
from tasks.create_raw_metadata import CreateRawMetadata
from tasks.create_raw_data import CreateRawData
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData


PLURALS = {
    'authors': 'author',
    'cite_spans': 'cite_span',
    'ref_spans': 'ref_span',
    'bib_entries': 'bib_entry',
    'other_ids': 'other_id',
    'ref_entries': 'ref_entry'
}


def create_schema(data_directory, raw_data_location, threads=1, force=False):
    project = HypergolProject(dataDirectory=data_directory, force=force)

    rawMetadata = project.datasetFactory.get(dataType=RawMetadata, name='raw_metadata')
    rawData = project.datasetFactory.get(dataType=RawData, name='raw_data')
    
    createRawMetadata = CreateRawMetadata(
        rawDataLocation=raw_data_location,
        splits=threads,
        outputDataset=rawMetadata
    )

    createRawData = CreateRawData(
        rawDataLocation=raw_data_location,
        plurals=PLURALS,
        inputDatasets=[rawMetadata],
        outputDataset=rawData,
        debug=True
    )

    pipeline = Pipeline(
        tasks=[
            # createRawMetadata,
            createRawData,
        ]
    )
    pipeline.run(threads=threads)


if __name__ == '__main__':
    fire.Fire(create_schema)
