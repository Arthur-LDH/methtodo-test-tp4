import json
import unittest

from src.credit_score_package.credit_score_updater import CreditScoreUpdater
from src.credit_score_package.exception.invalid_empty_csv_file import InvalidEmptyCsvFile
from src.credit_score_package.exception.invalid_number_of_columns import InvalidNumberOfColumns
from src.credit_score_package.exception.invalid_wrong_headers_csv_file import InvalidWrongHeadersCsvFile


class CreditScoreInterfaceTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.csi = None

    def setUp(self):
        self.csi = CreditScoreUpdater('../fixtures/source.csv')
        self.database = self.csi.load_database_string('../fixtures/database.json')

    def tearDown(self):
        with open('../fixtures/database.json', 'w') as json_file:
            json.dump(self.database, json_file)

    def test_exec_with_empty_csv_file(self):
        with self.assertRaises(InvalidEmptyCsvFile):
            CreditScoreUpdater('../fixtures/empty.csv').exec()

    def test_exec_with_csv_file_with_wrong_headers(self):
        with self.assertRaises(InvalidWrongHeadersCsvFile):
            CreditScoreUpdater('../fixtures/wrong_headers.csv').exec()

    def test_exec_with_wrong_number_of_columns(self):
        with self.assertRaises(InvalidNumberOfColumns):
            CreditScoreUpdater('../fixtures/wrong_number_of_columns.csv').exec()

    def test_load_database_string(self):
        # Assuming you have a test_database.json file with {"test": "data"} as content
        result = self.csi.load_database_string('../fixtures/database.json')
        expected_result = {"1": {"credit_score": 769,"datetime": "2024-04-30T13:19:59"}}
        self.assertEqual(result, expected_result)
    def test_exec(self):
        result = CreditScoreUpdater('../fixtures/test_invalid_datetime.csv').exec()
        expected_result = [{'index': 0, 'status_code': 0, 'status_message': 'FAILED: Invalid number of columns', 'line': ['1', '2024-05-04T13:19:59']}]
        self.assertEqual(result, expected_result)

