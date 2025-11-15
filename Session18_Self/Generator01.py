def simple_gen():
    yield 1
    yield 2

gen = simple_gen()
print(list(gen))