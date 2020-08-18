import unittest
from challenge import counter


class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        self.assertEqual(counter("Leksus"), 6)

    def test_easy_input_two(self):
        self.assertEqual(counter("Alina"), 5)


class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        # Todo: make sure that the program raises an exception whenever there is any non-english charts. Ex. !@#$%^.
        with self.assertRaises(TypeError):
            self.assertEqual(counter("Alin@"), 5)


    def test_medium_input_two(self):
        # Todo: make sure that your program does not count paces. It should only count english alpha.
        self.assertEqual(counter("Alina Kotik"), 10)


class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        # Todo: make sure that the program raises an exception whenever an empty string is given.
        with self.assertRaises(TypeError):
            self.assertEqual(counter(""), 0)

    def test_hard_input_two(self):
        # Todo: make sure that your program does not accept a None input.
        with self.assertRaises(TypeError):
            self.assertEqual(counter(None), 0)

    def test_hard_input_three(self):
        # Todo: make sure that your program assert only string.
        with self.assertRaises(TypeError):
            self.assertEqual(counter(41), 0)


if __name__ == '__main__':
    unittest.main()
