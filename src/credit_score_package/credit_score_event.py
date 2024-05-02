class CreditScoreEvent:
    def __init__(self):
        self.lines = []

    def add_line(self, status, status_message, line, index):
        self.lines.append({
            'index': index,
            'status_code': status,
            'status_message': status_message,
            'line': line
        })

    def get_failed_lines(self):
        for line in self.lines:
            if line['status_code'] == 0:
                print(line)