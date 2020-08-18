import sys
import unittest
from io import StringIO
from challenge_3 import Printer


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_value_name(self):
        # Todo: use the object printer to add the name 'Muhammad Ali' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Muhammad Ali'
        self.printer.set_value("Aleks")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), "Aleks")

    def test_value_job(self):
        # Todo: use the object printer to add the job 'Boxer' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Boxer'
        # Todo: use assertEqual to check if the printed string is 'Muhammad Ali'
        self.printer.set_value("IT")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), "IT")

    def tearDown(self):
        self.printer = None


if __name__ == '__main__':
    unittest.main()
