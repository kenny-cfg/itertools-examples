import itertools


def get_fizz_buzz_response(source_number, fizz, buzz):
    if source_number % buzz == 0:
        if source_number % fizz == 0:
            return "fizz buzz"
        return "buzz"
    if source_number % fizz == 0:
        return "fizz"
    return f"{source_number}"


def get_fizz_buzz_iterator(fizz=5, buzz=7):
    positive_integers = itertools.count(start=1, step=1)
    iterator = (get_fizz_buzz_response(x, fizz, buzz) for x in positive_integers)
    return iterator
