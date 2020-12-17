import fire
from hypergol import HypergolProject
from hypergol import Pipeline
from tasks.create_schema import CreateSchema


def create_schema_commands(threads=1, force=False):
    project = HypergolProject(dataDirectory='.', force=force)
    createSchema = CreateSchema(
        inputDatasets=[exampleInputDataset1,  exampleInputDataset2],
        outputDataset=exampleOutputDataset,
    )

    pipeline = Pipeline(
        tasks=[
            createSchema,
        ]
    )
    pipeline.run(threads=threads)


if __name__ == '__main__':
    fire.Fire(create_schema_commands)
