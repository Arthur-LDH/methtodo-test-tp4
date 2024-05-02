import unittest

from src.credit_score_package import CreditScoreInterface


class CreditScoreInterfaceTest(unittest.TestCase):
    def test_exec_with_empty_csv_file(self):
        with self.assertRaises(Exception):
            CreditScoreInterface('empty.csv').exec()

    def test_exec_with_csv_file_with_wrong_headers(self):
        with self.assertRaises(Exception):
            CreditScoreInterface('wrong_headers.csv').exec()

    def test_exec_with_csv_file_with_no_data(self):
        with self.assertRaises(Exception):
            CreditScoreInterface('no_data.csv').exec()

