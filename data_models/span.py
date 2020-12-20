from hypergol import BaseData


class Span(BaseData):

    def __init__(self, start: int, end: int, value: str):
        self.start = start
        self.end = end
        self.value = value
