import unittest

from src.credit_score_package import CreditScoreInterface
from src.credit_score_package.exception.invalid_empty_csv_file import InvalidEmptyCsvFile
from src.credit_score_package.exception.invalid_wrong_headers_csv_file import InvalidWrongHeadersCsvFile


class CreditScoreInterfaceTest(unittest.TestCase):
    def test_exec_with_empty_csv_file(self):
        with self.assertRaises(InvalidEmptyCsvFile):
            CreditScoreInterface('../../fixtures/empty.csv').exec()

    def test_exec_with_csv_file_with_wrong_headers(self):
        with self.assertRaises(InvalidWrongHeadersCsvFile):
            CreditScoreInterface('../../fixtures/wrong_headers.csv').exec()

    def test_exec_with_csv_file_with_no_data(self):
        with self.assertRaises(InvalidEmptyCsvFile):
            CreditScoreInterface('../../fixtures/no_data.csv').exec()

