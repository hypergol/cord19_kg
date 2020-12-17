import csv
from itertools import islice
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
        csvReader = csv.DictReader(open(f'{self.rawDataLocation}/metadata.csv','rt'))
        for row in islice(csvReader, parameters['split'], None, self.splits):
            if row['pdf_json_files'] != '' and row['pmc_json_files'] != '':
                yield (row, )

    def run(self, row):
        self.output.append(
            RawMetadata(
                cordUid=row['cord_uid'],
                sha=row['sha'],
                sourceX=row['source_x'],
                title=row['title'],
                doi=row['doi'],
                pmcid=row['pmcid'],
                pubmedId=row['pubmed_id'],
                license=row['license'],
                abstract=row['abstract'],
                publishTime=row['publish_time'],
                authors=row['authors'],
                journal=row['journal'],
                magId=row['mag_id'],
                whoCovidenceId=row['who_covidence_id'],
                arxivId=row['arxiv_id'],
                pdfJsonFiles=row['pdf_json_files'],
                pmcJsonFiles=row['pmc_json_files'],
                url=row['url'],
                s2Id=row['s2_id'],
            )
        )
