from hypergol import Task
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData
from data_models.article import Article


class CreateArticles(Task):

    def __init__(self, exampleParameter, *args, **kwargs):
        super(CreateArticles, self).__init__(*args, **kwargs)

    def run(self, rawData):
        
        self.output.append(exampleOutputObject)
