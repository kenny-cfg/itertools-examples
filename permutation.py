import itertools

permutation_iterable = itertools.permutations('ABC')
combination_iterable = itertools.combinations('ABC', 2)
powerset_iterable = itertools.chain.from_iterable([itertools.combinations('ABC', x) for x in range(0, 4)])

if __name__ == "__main__":
    print('Permutations:')
    for x in permutation_iterable:
        print(x)
    print('Combinations:')
    for x in combination_iterable:
        print(x)
    print('Powerset:')
    for x in powerset_iterable:
        print(x)