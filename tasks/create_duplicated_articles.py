from hypergol import Task
from hypergol.utils import get_hash
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData
from data_models.article import Article


class CreateDuplicatedArticles(Task):

    def __init__(self, exampleParameter, *args, **kwargs):
        super(CreateDuplicatedArticles, self).__init__(*args, **kwargs)

    def run(self, rawData):
        def _optional(value):
            if value is None:
                return []
            return [value]

        def get_name(author):
            nameParts = [author['first']] + author['middle'] + [author['last']]
            return ' '.join(nameParts))

        def get_other_id(bibEntry, name):
            return bibEntry['other_ids'].get(name, None) or []

        metadata = rawData.rawMetadata
        mainArticle = Article(
            articleId=get_hash(metadata.title),
            cordUid=rawData.cordUid,
            paperIds=[]
            title=metadata.title,
            authors=[author.strip() for author in rawData.rawMetadata.authors.split(';')],
            journal=rawData.rawMetadata.journal,
            DOI=_optional(rawData.rawMetadata.DOI),
            arXiv=_optional(rawData.rawMetadata.arXiv),
            PMID=_optional(rawData.rawMetadata.PMID),
            PMCID=_optional(rawData.rawMetadata.PMCID),
            year=_optional(rawData.rawMetadata.year)
        )
        for data in rawData.data:
            data = json.loads(data)
            mainArticle.paperIds.append(data['paper_id'])
            if data['metadata']['title'] != mainArticle.title:
                print('title mismatch')
                print(data['metadata']['title'])
                print(mainArticle.title)
            for author in data['metadata']['authors']:
                mainArticle.authors.append(get_name(author))
            for bibEntry in data['bib_entries']:
                self.output.append(Article(
                    articleId=get_hash(bibEntry['title']),
                    cordUid='',
                    paperIds=[],
                    title=bibEntry['title'],
                    authors=[get_name(author) for bibEntry['authors']],
                    journal=rawData.rawMetadata.journal,
                    DOI=get_other_id(bibEntry, 'DOI'),
                    arXiv=get_other_id(bibEntry, 'arXiv'),
                    PMID=get_other_id(bibEntry, 'PMID'),
                    PMCID=get_other_id(bibEntry, 'PMCID'),
                    year=_optional(bibEntry['year'])
                ))
        self.output.append(mainArticle)
