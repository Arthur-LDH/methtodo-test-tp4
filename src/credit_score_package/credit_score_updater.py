import csv
import json
from datetime import datetime

from sqlalchemy import between

from .credit_score_event import CreditScoreEvent
from .exception.invalid_empty_csv_file import InvalidEmptyCsvFile
from .exception.invalid_number_of_columns import InvalidNumberOfColumns
from .exception.invalid_wrong_headers_csv_file import InvalidWrongHeadersCsvFile


class CreditScoreUpdater:
    def __init__(self, file_path):
        self.status_message = 'SUCCESS'
        self.status = 1
        self.credit_score_event = CreditScoreEvent()
        self.file_path = file_path
        self.database = self.load_database_string()

    def load_database_string(self, database_path='fixtures/database.json'):
        with open(database_path, 'r') as file:
            data = json.load(file)
        return data

    def exec(self):
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
                self.__exec_line(row, index)
                index += 1
                pass

        return self.credit_score_event.get_failed_lines()

    def __exec_line(self, line, index):
        # Parse line[0] and line[2] to int
        line[0] = int(line[0])
        line[2] = int(line[2])
        # Parse line[1] to datetime
        line[1] = datetime.fromisoformat(line[1])

        if not self.__check_if_csv_columns_are_valids(line):
            self.status = 0
            self.status_message = 'FAILED: Invalid number of columns'
            self.credit_score_event.add_line(self.status, self.status_message, line, index)
            return

        if not self.__check_if_line_exists_in_database(line):
            self.status = 0
            self.status_message = 'FAILED: Line does not exist in database'
            self.credit_score_event.add_line(self.status, self.status_message, line, index)
            return

        if not self.__check_if_timestamp_is_valid(line):
            self.status = 0
            self.status_message = 'FAILED: Invalid timestamp'
            self.credit_score_event.add_line(self.status, self.status_message, line, index)
            return

        self.__update_line(line)
        self.credit_score_event.add_line(self.status, self.status_message, line, index)

    def __check_if_csv_columns_are_valids(self, line):
        if len(line) != 3:
            print('len(line) is not 3')
            return False
        if not isinstance(line[0], int):
            print('line[0] is not int')
            return False
        if not isinstance(line[1], datetime):
            print('line[1] is not datetime')
            return False
        if not isinstance(line[2], int) and not between(line[2], 300, 800):
            print('line[2] is not int or not between 300 and 800')
            return False
        return True

    def __check_if_line_exists_in_database(self, line):
        if str(line[0]) not in self.database:
            return False
        return True

    def __check_if_timestamp_is_valid(self, line):
        if line[1] <=  datetime.fromisoformat(self.database[str(line[0])]['datetime']):
            return False
        return True

    def __update_line(self, line):
        self.database[str(line[0])]['datetime'] = line[1].isoformat()
        self.database[str(line[0])]['credit_score'] = line[2]

        with open('fixtures/database.json', 'w') as json_file:
            json.dump(self.database, json_file)
