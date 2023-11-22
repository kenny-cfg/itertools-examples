import itertools

even_numbers = itertools.count(start=0, step=2)
multiples_of_five = itertools.count(start=0, step=5)

if __name__ == '__main__':
    print('Some even numbers')
    count = 100
    for x in even_numbers:
        print(x)
        count -= 1
        if count < 0:
            break
    print('Some multiples of 5')
    count = 100
    for x in multiples_of_five:
        print(x)
        count -= 1
        if count < 0:
            break

# Make an iterable of all multiples of 5
