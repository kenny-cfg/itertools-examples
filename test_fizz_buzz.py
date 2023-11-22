import itertools
import unittest

from fizz_buzz import get_fizz_buzz_iterator


class FizzBuzzTest(unittest.TestCase):
    def test_first_four_numbers(self):
        iterator = get_fizz_buzz_iterator()
        first_four_items = list(itertools.islice(iterator, 0, 4))
        self.assertEqual(first_four_items, ["1", "2", "3", "4"])


if __name__ == '__main__':
    unittest.main()
