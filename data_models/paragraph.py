from typing import List

from hypergol import BaseData


class Paragraph(BaseData):

    def __init__(self, articleId: str, paragraphId: int, text: str, citations: List[str]):
        self.articleId = articleId
        self.paragraphId = paragraphId
        self.text = text
        self.citations = citations

    def get_id(self):
        return (self.articleId, self.paragraphId, )

    # # This is to keep all the paragraph of the same article in the same chunk
    # def get_hash_id(self):
    #     return (self.articleId, )
