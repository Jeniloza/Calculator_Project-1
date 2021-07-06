import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('addition.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader