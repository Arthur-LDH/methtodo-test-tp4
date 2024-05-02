class InvalidWrongHeadersCsvFile(Exception):
    def __init__(self, message="Invalid CSV file: wrong headers"):
        super().__init__(message)