from CsvReader import CsvReader

def addition(a, b):
    c = int(a) + int(b)
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

