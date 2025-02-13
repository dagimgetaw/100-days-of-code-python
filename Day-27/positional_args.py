def add(*args):
    print(args)
    total = 0
    for n in args:
        total += n

    return total


x = add(2, 3, 4, 5, 6)

print(x)
