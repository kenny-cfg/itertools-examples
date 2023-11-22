import itertools


def get_fizz_buzz_response(source_number, fizz, buzz):
    is_fizz = source_number % fizz == 0
    is_buzz = source_number % buzz == 0
    if is_fizz and is_buzz:
        return "fizz buzz"
    if is_buzz:
        return "buzz"
    if is_fizz:
        return "fizz"
    return f"{source_number}"


def get_fizz_buzz_iterator(fizz=5, buzz=7):
    positive_integers = itertools.count(start=1, step=1)
    iterator = (get_fizz_buzz_response(x, fizz, buzz) for x in positive_integers)
    return iterator
