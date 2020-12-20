from typing import List

from hypergol import BaseData


class Paragraph(BaseData):

    def __init__(self, articleId: str, paperId: str, paragraphNumber: int, text: str, citations: List[str]):
        self.articleId = articleId
        self.paperId = paperId
        self.paragraphNumber = paragraphNumber
        self.text = text
        self.citations = citations

    def get_id(self):
        return (self.articleId, self.paperId, self.paragraphNumber, )

    # # This is to keep all the paragraph of the same article in the same chunk
    # def get_hash_id(self):
    #     return (self.articleId, )
