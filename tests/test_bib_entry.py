from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.bib_entry import BibEntry


class TestBibEntry(TestCase):

    def __init__(self, methodName):
        super(TestBibEntry, self).__init__(methodName=methodName)
        self.bibEntry = BibEntry(refId='', title='', authors=['', ''], year=[0, 0], venue='', volume='', issn='', pages='', DOI=['', ''], arXiv=['', ''], PMID=['', ''], PMCID=['', ''], bibEntryId='')

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_bib_entry_test_get_hash_id(self):
        self.assertEqual(self.bibEntry.test_get_hash_id(), True)

    def test_bib_entry_test_to_data(self):
        self.assertEqual(self.bibEntry.test_to_data(), True)

    def test_bib_entry_test_from_data(self):
        self.assertEqual(self.bibEntry.test_from_data(), True)
