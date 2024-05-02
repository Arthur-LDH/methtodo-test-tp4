class InvalidEmptyCsvFile(Exception):
    def __init__(self, message="Invalid CSV file"):
        super().__init__(message)