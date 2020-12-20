from hypergol import Task
from hypergol.utils import get_hash
from data_models.span import Span
from data_models.raw_metadata import RawMetadata
from data_models.raw_data import RawData
from data_models.paragraph import Paragraph


class CreateParagraphs(Task):

    def __init__(self, exampleParameter, *args, **kwargs):
        super(CreateParagraphs, self).__init__(*args, **kwargs)

    def run(self, rawData):
        for data in rawData.data:
            data = json.loads(data)
            bibArticles = {
                bibEntry['bib_entry_id']: get_hash(bibEntry['title']) 
                for bibEntry in data['bib_entries'] 
            }
            rawParagraphs = data['abstract'] + data['body_text'] + data['back_matter']
            for paragraphNumber, rawParagraph in rawParagraphs:
                 self.output.append(Paragraph(
                    articleId=get_hash(rawData['metadata']['title']),
                    paperId=data['paper_id'],
                    paragraphNumber=paragraphNumber,
                    text=rawParagraph['text'],
                    citations=[Span(
                        start=rawParagraph['cite_spans']['start'],
                        end=rawParagraph['cite_spans']['end'],
                        value=bibArticles[rawParagraph['cite_spans']['ref_id']]
                    ) for span in rawParagraph['cite_spans'] if span['ref_id'] is not None]
                ))
