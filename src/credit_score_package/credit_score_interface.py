import csv
import json

from .credit_score_event import CreditScoreEvent
from .exception.invalid_empty_csv_file import InvalidEmptyCsvFile
from .exception.invalid_number_of_columns import InvalidNumberOfColumns
from .exception.invalid_wrong_headers_csv_file import InvalidWrongHeadersCsvFile


class CreditScoreInterface:
    def __init__(self, file_path):
        self.file_path = file_path
        self.database = self.load_database_string()

    def load_database_string(self, database_path='../fixtures/database.json'):
        with open(database_path, 'r') as file:
            data = json.load(file)
        return str(data)


    def exec(self):
        # instantiate the credit score event
        credit_score_event = CreditScoreEvent()

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader, None)

            if headers is None:
                raise InvalidEmptyCsvFile()

            if len(headers) != 3:
                raise InvalidNumberOfColumns()

            expected_headers = ['id', 'datetime', 'credit_score']
            if headers != expected_headers:
                raise InvalidWrongHeadersCsvFile()

            # Execute each row
            index = 0
            for row in reader:
                self.exec_line(credit_score_event, row, index)
                index += 1
                pass

    def exec_line(self, credit_score_event, line, index):
        # // logic to verify if the line is valid
        status = 1
        status_message = 'SUCCESS'

        if len(line) != 3:
            status = 0
            status_message = 'FAILED: Invalid number of columns'


        # else:
        #     // logic to insert a new line


        credit_score_event.add_line(status, status_message, line, index)





        # // logic to parse the line

        # // logic to insert the line into the event

        # line = {
        #     1: {
        #         'credit_score': 800,
        #         'datetime': '2024 - 12 - 12 12: 12: 12 ',
        #         'status_code': 1,
        #         'status_message': 'SUCCESS'
        #     }
        # }
        #
        #
        # # if status_code = 1:
        # #     self.insert_line(line)
        #
        # return;

    def check_if_line_exists(self, id):
        # // logic to check if the line exists
        return False;

    def update_line(self, line):

        return;
