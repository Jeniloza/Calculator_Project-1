import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/add.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(row['\ufeffValue 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/subtraction.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['\ufeffValue 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_method_calculator(self):
        test_data = CsvReader('/src/multiplication.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiplication(row['\ufeffValue 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_data = CsvReader('/src/division.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.division(row['\ufeffValue 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_sqrnum_method_calculator(self):
        test_data = CsvReader('/src/sqr.csv').data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.sqrnum(row['\ufeffValue 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrroot_method_calculator(self):
        test_data = CsvReader('/src/sqrroot.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.sqrroot(row['\ufeffValue 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

if __name__ == '__main__':
    unittest.main()