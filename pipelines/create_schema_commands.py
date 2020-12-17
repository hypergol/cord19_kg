import fire
from hypergol import HypergolProject
from hypergol import Pipeline
from tasks.create_metadata import CreateMetadata
from tasks.create_schema import CreateSchema


def create_schema_commands(data_location, threads=1, force=False):
    project = HypergolProject(dataDirectory='.', force=force)

    createSchema = CreateMetadata(
        outputDataset=None,
    )

    createSchema = CreateSchema(
        outputDataset=None,
    )

    pipeline = Pipeline(
        tasks=[
            createSchema,
        ]
    )
    pipeline.run(threads=threads)


if __name__ == '__main__':
    fire.Fire(create_schema_commands)
