from .credit_score_event import CreditScoreEvent


class CreditScoreInterface:
    def __init__(self, file_path):
        self.file_path = file_path

    def exec(self):
        # instantiate the credit score event
        credit_score_event = CreditScoreEvent()

        # check if the csv file is valid
        with open(self.file_path, 'r') as file:
            for line in file:
                self.exec_line(credit_score_event, line)

    def exec_line(self, credit_score_event, line):


        # // logic to verify if the line is valid

        # // logic to parse the line

        # // logic to insert the line into the event

        line = {
            1: {
                'credit_score': 800,
                'datetime': '2024 - 12 - 12 12: 12: 12 ',
                'status_code': 1,
                'status_message': 'SUCCESS'
            }
        }

        credit_score_event.add_line(line)

        # if status_code = 1:
        #     self.insert_line(line)

        return;

    def check_if_line_exists(self, id):
        # // logic to check if the line exists
        return False;

    def insert_line(self, line):
        # if check_if_line_exists(id):
        #     // logic to update an exsitng line
        # else:
        #     // logic to insert a new line
        return;
