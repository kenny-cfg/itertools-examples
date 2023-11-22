import itertools
import unittest

from fizz_buzz import get_fizz_buzz_iterator


class FizzBuzzTest(unittest.TestCase):
    def test_first_four_numbers(self):
        iterator = get_fizz_buzz_iterator()
        first_four_items = list(itertools.islice(iterator, 0, 4))
        self.assertEqual(first_four_items, ["1", "2", "3", "4"])

    def test_fifth_number_is_fizz(self):
        iterator = get_fizz_buzz_iterator()
        fifth_item = itertools.islice(iterator, 4, 5).__next__()
        self.assertEqual(fifth_item, "fizz")


if __name__ == '__main__':
    unittest.main()
