import unittest
from Calculator import Calculator
from CSVReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
#    def test_something(self):
#        self.assertEqual(True, False)

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator,Calculator)

    def test_addition(self):
        calculator = Calculator()
        testData = CsvReader('src/Unit Test Addition.csv').data #.return_data_as_objects('addition')
        for row in testData:
            self.assertEqual(calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            #self.assertEqual(calculator.result,row['Result'])

    def test_subtraction(self):
        calculator = Calculator()
        testData = CsvReader('src/Unit Test Subtraction.csv').data
        for row in testData:
            #print('Value 1:', row['Value 1'], 'Value 2', row['Value 2'], 'Result', row['Result'], 'Answer', calculator.subtract(int(row['Value 1']), int(row['Value 2'])))
            self.assertEqual(calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_division(self):
        calculator = Calculator()
        testData = CsvReader('src/Unit Test Division.csv').data
        for row in testData:
            decimal_at = row['Result'].find('.')
            precision = len(row['Result']) - decimal_at - 1
            if decimal_at == -1:
                precision = 0
            self.assertEqual(round(calculator.divide(int(row['Value 1']), int(row['Value 2'])),precision), round(float(row['Result']),precision))

    def test_multiplication(self):
        calculator = Calculator()
        testData = CsvReader('src/Unit Test Multiplication.csv').data
        for row in testData:
            self.assertEqual(calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_squared(self):
        calculator = Calculator()
        testData = CsvReader('src/Unit Test Square.csv').data
        for row in testData:
            self.assertEqual(calculator.square(int(row['Value 1'])), int(row['Result']))

    def test_squarerooted(self):
        calculator = Calculator()
        testData = CsvReader('src/Unit Test Square Root.csv').data

        for row in testData:
            decimal_at = row['Result'].find('.')
            precision = len(row['Result']) - decimal_at - 1
            if decimal_at == -1:
                precision = 0

            self.assertEqual(round(calculator.squareroot(int(row['Value 1'])),precision), round(float(row['Result']),precision))


if __name__ == '__main__':
    unittest.main()
