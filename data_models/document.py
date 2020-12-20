from typing import List

from hypergol import BaseData


class Document(BaseData):

    def __init__(self, documentId: int, tokens: List[str], labels: List[str]):
        self.documentId = documentId
        self.tokens = tokens
        self.labels = labels

    def get_id(self):
        return (self.documentId, )
