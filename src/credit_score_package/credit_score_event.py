class CreditScoreEvent:
    def __init__(self):
        self.failed_lines = []

    def add_line(self, status, status_message, line, index):
        if status == 0:
            self.failed_lines.append({
                'index': index,
                'status_code': status,
                'status_message': status_message,
                'line': line
            })

    def get_failed_lines(self):
        return self.failed_lines
