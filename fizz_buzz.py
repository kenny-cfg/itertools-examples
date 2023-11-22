import itertools


def get_fizz_buzz_iterator():
    positive_integers = itertools.count(start=1, step=1)
    iterator = (f"{x}" for x in positive_integers)
    return iterator
