from hypergol import BaseData


class RawMetadata(BaseData):

    def __init__(self, cordUid: str, sha: str, sourceX: str, title: str, doi: str, pmcid: str, pubmedId: str, license: str, abstract: str, publishTime: str, authors: str, journal: str, magId: str, whoCovidenceId: str, arxivId: str, pdfJsonFiles: str, pmcJsonFiles: str, url: str, s2Id: str):
        self.cordUid = cordUid
        self.sha = sha
        self.sourceX = sourceX
        self.title = title
        self.doi = doi
        self.pmcid = pmcid
        self.pubmedId = pubmedId
        self.license = license
        self.abstract = abstract
        self.publishTime = publishTime
        self.authors = authors
        self.journal = journal
        self.magId = magId
        self.whoCovidenceId = whoCovidenceId
        self.arxivId = arxivId
        self.pdfJsonFiles = pdfJsonFiles
        self.pmcJsonFiles = pmcJsonFiles
        self.url = url
        self.s2Id = s2Id
