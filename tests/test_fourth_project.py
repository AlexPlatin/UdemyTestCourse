import unittest
import time
from fourth_project import FibonacciSequence


class TestEfficiency(unittest.TestCase):
    def setUp(self) -> None:
        self._fibon = FibonacciSequence()
        self._efficiency_data = dict()

    def test_first_method(self):
        starting_time = time.perf_counter()
        self._fibon.recursive_method(35)
        ending_time = time.perf_counter()
        self._efficiency_data["recursive"] = ending_time - starting_time
        print(self._efficiency_data)

    def test_second_method(self):
        starting_time = time.perf_counter()
        self._fibon.math_method(35)
        ending_time = time.perf_counter()
        self._efficiency_data["math_method"] = ending_time - starting_time
        print(self._efficiency_data)

    def tearDown(self) -> None:
        self._fibon = None

if __name__ == '__main__':
    unittest.main()
