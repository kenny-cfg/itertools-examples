import itertools


def get_fizz_buzz_response(source_number):
    if source_number % 7 == 0:
        return "buzz"
    if source_number % 5 == 0:
        return "fizz"
    return f"{source_number}"


def get_fizz_buzz_iterator():
    positive_integers = itertools.count(start=1, step=1)
    iterator = (get_fizz_buzz_response(x) for x in positive_integers)
    return iterator
