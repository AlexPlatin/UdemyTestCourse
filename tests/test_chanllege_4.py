import time
import unittest
from challenge_4 import EfficiencyAdding


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._efficiency = EfficiencyAdding()
        self._efficiency_data = dict()

    def test_first_adding_method(self):
        start = time.perf_counter()
        self._efficiency.adding_two_first_method(100)
        finish = time.perf_counter()
        self._efficiency_data["first"] = finish - start

    def test_second_adding_method(self):
        start = time.perf_counter()
        self._efficiency.adding_two_second_method(100)
        finish = time.perf_counter()
        self._efficiency_data["second"] = finish - start

    def tearDown(self):
        print(self._efficiency_data)
        self._efficiency = None


if __name__ == '__main__':
    unittest.main()
