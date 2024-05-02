import sys
from credit_score_package import CreditScoreUpdater

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        raise Exception('Insufficient Arguments')
    CreditScoreUpdater(args[0]).exec()
