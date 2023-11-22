import itertools

cycle_iterable = itertools.cycle('123456')
cycle_iterable_2 = itertools.cycle([5, 10, 15, 12])

if __name__ == "__main__":
    count = 50
    for x in cycle_iterable_2:
        print(x)
        count -= 1
        if count < 0:
            break