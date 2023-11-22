import itertools

chain_iterable = itertools.chain('ABC', 'DEF', 'POO')

if __name__ == "__main__":
    for x in chain_iterable:
        print(x)