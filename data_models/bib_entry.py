from typing import List

from hypergol import BaseData


class BibEntry(BaseData):

    def __init__(self, paperId: str, bibNumber: int, title: str, authors: List[str], year: List[int], doi: List[str], arxiv: List[str], pmid: List[str], pmcid: List[str]):
        self.paperId = paperId
        self.bibNumber = bibNumber
        self.title = title
        self.authors = authors
        self.year = year
        self.doi = doi
        self.arxiv = arxiv
        self.pmid = pmid
        self.pmcid = pmcid

    def get_id(self):
        return (self.paperId, self.bibNumber)