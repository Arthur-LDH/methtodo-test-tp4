import unittest

from src.credit_score_package.credit_score_interface import CreditScoreInterface
from src.credit_score_package.exception.invalid_empty_csv_file import InvalidEmptyCsvFile
from src.credit_score_package.exception.invalid_number_of_columns import InvalidNumberOfColumns
from src.credit_score_package.exception.invalid_wrong_headers_csv_file import InvalidWrongHeadersCsvFile


class CreditScoreInterfaceTest(unittest.TestCase):
    def test_exec_with_empty_csv_file(self):
        with self.assertRaises(InvalidEmptyCsvFile):
            CreditScoreInterface('../fixtures/empty.csv').exec()

    def test_exec_with_csv_file_with_wrong_headers(self):
        with self.assertRaises(InvalidWrongHeadersCsvFile):
            CreditScoreInterface('../fixtures/wrong_headers.csv').exec()

    def test_exec_with_wrong_number_of_columns(self):
        with self.assertRaises(InvalidNumberOfColumns):
            CreditScoreInterface('../fixtures/wrong_number_of_columns.csv').exec()

