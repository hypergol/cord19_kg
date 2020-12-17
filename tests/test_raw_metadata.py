from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.raw_metadata import RawMetadata


class TestRawMetadata(TestCase):

    def __init__(self, methodName):
        super(TestRawMetadata, self).__init__(methodName=methodName)
        self.rawMetadata = RawMetadata(cordUid='', sha='', sourceX='', title='', doi='', pmcid='', pubmedId='', license='', abstract='', publishTime='', authors='', journal='', magId='', whoCovidenceId='', arxivId='', pdfJsonFiles='', pmcJsonFiles='', url='', s2Id='')

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_raw_metadata_test_get_hash_id(self):
        self.assertEqual(self.rawMetadata.test_get_hash_id(), True)

    def test_raw_metadata_test_to_data(self):
        self.assertEqual(self.rawMetadata.test_to_data(), True)

    def test_raw_metadata_test_from_data(self):
        self.assertEqual(self.rawMetadata.test_from_data(), True)
