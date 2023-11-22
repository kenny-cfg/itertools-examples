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

    def test_tenth_number_is_fizz(self):
        iterator = get_fizz_buzz_iterator()
        fifth_item = itertools.islice(iterator, 9, 10).__next__()
        self.assertEqual(fifth_item, "fizz")

    def test_seventh_number_is_buzz(self):
        iterator = get_fizz_buzz_iterator()
        fifth_item = itertools.islice(iterator, 6, 7).__next__()
        self.assertEqual(fifth_item, "buzz")

    def test_fourteenth_number_is_buzz(self):
        iterator = get_fizz_buzz_iterator()
        fifth_item = itertools.islice(iterator, 13, 14).__next__()
        self.assertEqual(fifth_item, "buzz")

    def test_number_35_is_fizzbuzz(self):
        iterator = get_fizz_buzz_iterator()
        fifth_item = itertools.islice(iterator, 34, 35).__next__()
        self.assertEqual(fifth_item, "fizz buzz")

if __name__ == '__main__':
    unittest.main()
