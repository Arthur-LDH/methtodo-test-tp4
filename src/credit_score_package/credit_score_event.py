class CreditScoreEvent:
    def __init__(self):
        self.lines = {}

    def add_line(self, status, status_message, line, index):

        self.lines.append(line)

        index: {
            'status_code': 0,
            'status_message': 'FAILED',
            'line': line

        }

        pass

    def get_failed_lines(self):
        # Return the line with status code 0 + status message 'FAILED + the details of the error'
        return 'failed_lines'
