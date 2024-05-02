from .credit_score_event import CreditScoreEvent


class CreditScoreInterface:
    def __init__(self, file_path):
        self.file_path = file_path

    def exec(self):
        credit_score_event = CreditScoreEvent()
        with open(self.file_path, 'r') as file:
            for line in file:
                self.exec_line(credit_score_event, line)

    def exec_line(self, credit_score_event, line):
        return;
