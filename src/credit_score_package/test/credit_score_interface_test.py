import unittest

from src.credit_score_package import CreditScoreInterface


class CreditScoreInterfaceTest(unittest.TestCase):
    def test_exec_with_empty_csv_file(self):
        with self.assertRaises(Exception):
            CreditScoreInterface('empty.csv').exec()

