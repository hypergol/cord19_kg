from datetime import time
from datetime import date
from datetime import datetime
from unittest import TestCase

from data_models.span import Span


class TestSpan(TestCase):

    def __init__(self, methodName):
        super(TestSpan, self).__init__(methodName=methodName)
        self.span = Span(start=0, end=0, value='')

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_span_test_get_hash_id(self):
        self.assertEqual(self.span.test_get_hash_id(), True)

    def test_span_test_to_data(self):
        self.assertEqual(self.span.test_to_data(), True)

    def test_span_test_from_data(self):
        self.assertEqual(self.span.test_from_data(), True)
