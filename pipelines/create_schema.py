import fire
from hypergol import HypergolProject
from hypergol import Pipeline
from tasks.create_raw_metadata import CreateRawMetadata
from tasks.create_raw_data import CreateRawData
from tasks.create_duplicated_articles import CreateDuplicatedArticles
from tasks.create_paragraphs import CreateParagraphs
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData
from data_models.article import Article
from data_models.paragraph import Paragraph


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

    rawMetadata = project.datasetFactory.get(dataType=RawMetadata, branch='master', name='raw_metadata', chunkCount=256)
    rawData = project.datasetFactory.get(dataType=RawData, branch='master', name='raw_data', chunkCount=256)
    duplicatedArticles = project.datasetFactory.get(dataType=Article, name='duplicatedArticles', chunkCount=256)
    paragraphs = project.datasetFactory.get(dataType=Paragraph, name='paragraphs', chunkCount=256)
    
    createRawMetadata = CreateRawMetadata(
        rawDataLocation=raw_data_location,
        splits=threads,
        outputDataset=rawMetadata
    )

    createRawData = CreateRawData(
        rawDataLocation=raw_data_location,
        plurals=PLURALS,
        inputDatasets=[rawMetadata],
        outputDataset=rawData
    )

    createDuplicatedArticles = CreateDuplicatedArticles(
        inputDatasets=[rawData],
        outputDataset=duplicatedArticles
    )

    createParagraphs = CreateParagraphs(
        inputDatasets=[rawData],
        outputDataset=paragraphs
    )

    pipeline = Pipeline(
        tasks=[
            # createRawMetadata,
            # createRawData,
            createDuplicatedArticles,
            # createParagraphs
        ]
    )
    pipeline.run(threads=threads)


if __name__ == '__main__':
    fire.Fire(create_schema)
