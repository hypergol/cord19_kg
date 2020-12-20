from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.paragraph import Paragraph


class TestParagraph(TestCase):

    def __init__(self, methodName):
        super(TestParagraph, self).__init__(methodName=methodName)
        self.paragraph = Paragraph(articleId='', paragraphId=0, text='', citations=['', ''])

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_paragraph_test_get_hash_id(self):
        self.assertEqual(self.paragraph.test_get_hash_id(), True)

    def test_paragraph_test_to_data(self):
        self.assertEqual(self.paragraph.test_to_data(), True)

    def test_paragraph_test_from_data(self):
        self.assertEqual(self.paragraph.test_from_data(), True)
