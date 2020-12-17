import fire
from hypergol import HypergolProject
from hypergol import Pipeline
from tasks.create_metadata import CreateMetadata
from tasks.create_schema import CreateSchema
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData


def create_schema(data_directory, raw_data_location, threads=1, force=False):
    project = HypergolProject(dataDirectory=data_directory, force=force)
    rawMetadatas = project.datasetFactory.get(dataType=RawMetadata, name='raw_metadatas')
    rawDatas = project.datasetFactory.get(dataType=RawData, name='raw_datas')
    createMetadata = CreateMetadata(
        inputDatasets=[exampleInputDataset1,  exampleInputDataset2],
        outputDataset=exampleOutputDataset,
    )
    createSchema = CreateSchema(
        inputDatasets=[exampleInputDataset1,  exampleInputDataset2],
        outputDataset=exampleOutputDataset,
    )

    pipeline = Pipeline(
        tasks=[
            createMetadata,
            createSchema,
        ]
    )
    pipeline.run(threads=threads)


if __name__ == '__main__':
    fire.Fire(create_schema)
