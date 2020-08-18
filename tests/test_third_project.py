import unittest
import sys
from io import StringIO
from third_project import Profile


class TestPrintOut(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile("Alesk", "25", "IT")

    def test_name(self):
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue().strip(), "Alesk")

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), "25")

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), "IT")

    def tearDown(self) -> None:
        self.profile = None

if __name__ == '__main__':
    unittest.main()
