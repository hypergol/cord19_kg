from hypergol import Job
from hypergol import Task
from data_models.raw_metadata import RawMetadata


class CreateRawMetadata(Task):

    def __init__(self, rawDataLocation, splits, *args, **kwargs):
        super(CreateRawMetadata, self).__init__(*args, **kwargs)
        self.rawDataLocation = rawDataLocation
        self.splits = splits

    def get_jobs(self):
        return [Job(
            id_=split, 
            total=self.splits,
            parameters={'split': split}
        ) for split in range(self.splits)]

    def source_iterator(self, parameters):
        metadata=pd.read_csv(f'{self.rawDataLocation}/metadata.csv')[:1000].fillna(0)
        split = parameters['split']
        for row in islice(metadata.itertuples(index=False), split, None, self.splits):
            if row.pdf_json_files != 0 and rawMetadata.pmc_json_files != 0:
                yield (row, )

    def run(self, row):
        self.output.append(
            RawMetadata(
                self.cordUid=row.cord_uid
                self.sha=row.sha
                self.sourceX=row.source_x
                self.title=row.title
                self.doi=row.doi
                self.pmcid=row.pmcid
                self.pubmedId=row.pubmed_id
                self.license=row.license
                self.abstract=row.abstract
                self.publishTime=row.publish_time
                self.authors=row.authors
                self.journal=row.journal
                self.magId=row.mag_id
                self.whoCovidenceId=row.who_covidence_id
                self.arxivId=row.arxiv_id
                self.pdfJsonFiles=row.pdf_json_files
                self.pmcJsonFiles=row.pmc_json_files
                self.url=row.url
                self.s2Id=row.s2_id
            )
        )
