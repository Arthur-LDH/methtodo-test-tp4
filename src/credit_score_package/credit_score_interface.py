import csv

from .credit_score_event import CreditScoreEvent


class CreditScoreInterface:
    def __init__(self, file_path):
        self.file_path = file_path

    def exec(self):
        # instantiate the credit score event
        credit_score_event = CreditScoreEvent()

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)

            if len(reader) == 0:
                raise Exception('CSV file is empty')

            # Check if headers are as expected
            expected_headers = ['id', 'datetime', 'credit_score']
            if headers != expected_headers:
                raise Exception('CSV file does not have the expected headers')

            if next(reader, None) is None:
                raise Exception('CSV file is empty')

            # Execute each row
            for row in reader:
                self.exec_line(credit_score_event, row)

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
