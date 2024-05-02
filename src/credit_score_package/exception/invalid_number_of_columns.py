class InvalidNumberOfColumns(Exception):
    def __init__(self, message="Invalid number of columns"):
        super().__init__(message)