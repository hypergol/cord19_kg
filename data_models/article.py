from typing import List

from hypergol import BaseData


class Article(BaseData):

    def __init__(self, articleId: str, paperId: str, title: str, authors: List[str], DOI: List[str], arXiv: List[str], PMID: List[str], PMCID: List[str], year: List[int]):
        self.articleId = articleId
        self.paperId = paperId
        self.title = title
        self.authors = authors
        self.DOI = DOI
        self.arXiv = arXiv
        self.PMID = PMID
        self.PMCID = PMCID
        self.year = year

    def get_id(self):
        return (self.articleId, )
