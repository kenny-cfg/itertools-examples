import unittest

from fizz_buzz import get_fizz_buzz_iterator


class FizzBuzzTest(unittest.TestCase):
    def test_first_four_numbers(self):
        iterator = get_fizz_buzz_iterator()


if __name__ == '__main__':
    unittest.main()
