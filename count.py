import itertools

even_numbers = itertools.count(start=0, step=2)

if __name__ == '__main__':
    count = 100
    for x in even_numbers:
        print(x)
        count -= 1
        if count < 0:
            break

