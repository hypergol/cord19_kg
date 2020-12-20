from hypergol import Task
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData
from data_models.bib_entry import BibEntry


class CollectBibEntries(Task):

    def __init__(self, *args, **kwargs):
        super(CollectBibEntries, self).__init__(*args, **kwargs)

    def run(self, rawData):
        def get_name(author):
            nameParts = [author['first']] + author['middle'] + [author['last']]
            return ' '.join(nameParts)
        
        def _optional(value):
            if value is None:
                return []
            return [value]

        for data in rawData.data:
            data = json.loads(data)
            for bibNumber, bibEntry in enumerate(data['bib_entries']):
                self.output.append(BibEntry(
                    paperId=data['paper_id'],
                    bibNumber=bibNumber,
                    title=bibEntry['title'],
                    authors=[get_name(author) for author in bibEntry['authors']],
                    year=_optional(bibEntry['year']),
                    doi=get_other_id(bibEntry, 'DOI'),
                    arxiv=get_other_id(bibEntry, 'arXiv'),
                    pmid=get_other_id(bibEntry, 'PMID'),
                    pmcid=get_other_id(bibEntry, 'PMCID'),
                ))


        raise NotImplementedError(f'{self.__class__.__name__} must implement run()')
        self.output.append(exampleOutputObject)
