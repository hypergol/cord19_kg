from hypergol import BaseData

from data_models.raw_metadata import RawMetadata


class RawData(BaseData):

    def __init__(self, cordUid: str, data: str, rawMetadata: RawMetadata):
        self.cordUid = cordUid
        self.data = data
        self.rawMetadata = rawMetadata

    def to_data(self):
        data = self.__dict__.copy()
        data['rawMetadata'] = data['rawMetadata'].to_data()
        return data

    @classmethod
    def from_data(cls, data):
        data['rawMetadata'] = RawMetadata.from_data(data['rawMetadata'])
        return cls(**data)
