def gen(max=0):
    n = 1
    while n < max:
        yield n
        n += 1
a = gen(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))



