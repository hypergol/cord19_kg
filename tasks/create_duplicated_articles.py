import json
from hypergol import Task
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData
from data_models.article import Article


class CreateDuplicatedArticles(Task):

    def __init__(self, *args, **kwargs):
        super(CreateDuplicatedArticles, self).__init__(*args, **kwargs)

    def run(self, rawData):
        def _optional(value):
            if value is None:
                return []
            return [value]

        def get_name(author):
            nameParts = [author['first']] + author['middle'] + [author['last']]
            return ' '.join(nameParts)

        def get_other_id(bibEntry, name):
            return bibEntry['other_ids'].get(name, None) or []

        metadata = rawData.rawMetadata
        mainArticle = Article(
            articleId=Article.get_title_hash(metadata.title),
            cordUid=rawData.cordUid,
            paperIds=[],
            title=metadata.title,
            authors=[author.strip() for author in metadata.authors.split(';')],
            journal=metadata.journal,
            doi=_optional(metadata.doi),
            arxivId=_optional(metadata.arxivId),
            pmcid=_optional(metadata.pmcid),
            year=int(metadata.publishTime[:4])
        )
        for data in rawData.data:
            data = json.loads(data)
            mainArticle.paperIds.append(data['paper_id'])
            if data['metadata']['title'] != mainArticle.articleId:
                print('title mismatch')
                print(data['metadata']['title'])
                print(mainArticle.title)
            for author in data['metadata']['authors']:
                mainArticle.authors.append(get_name(author))
            for bibEntry in data['bib_entries']:
                self.output.append(Article(
                    articleId=Article.get_title_hash(bibEntry['title']),
                    cordUid='',
                    paperIds=[],
                    title=bibEntry['title'],
                    authors=[get_name(author) for author in bibEntry['authors']],
                    journal=rawData.rawMetadata.journal,
                    doi=get_other_id(bibEntry, 'DOI'),
                    arxivId=get_other_id(bibEntry, 'arXiv'),
                    pmcid=get_other_id(bibEntry, 'PMCID'),
                    year=_optional(bibEntry['year'])
                ))
        self.output.append(mainArticle)
