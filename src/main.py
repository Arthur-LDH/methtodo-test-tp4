import sys
from credit_score_package import CreditScoreInterface

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
        raise Exception ('Insufficient Arguments')
    CreditScoreInterface(args[0]).exec()