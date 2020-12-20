from typing import List

from hypergol import BaseData

from data_models.article import Article
from data_models.paragraph import Paragraph


class ArticleText(BaseData):

    def __init__(self, articleId: str, article: Article, paragraphs: List[Paragraph]):
        self.articleId = articleId
        self.article = article
        self.paragraphs = paragraphs

    def get_id(self):
        return (self.articleId, )

    def to_data(self):
        data = self.__dict__.copy()
        data['article'] = data['article'].to_data()
        data['paragraphs'] = [v.to_data() for v in data['paragraphs']]
        return data

    @classmethod
    def from_data(cls, data):
        data['article'] = Article.from_data(data['article'])
        data['paragraphs'] = [Paragraph.from_data(v) for v in data['paragraphs']]
        return cls(**data)
