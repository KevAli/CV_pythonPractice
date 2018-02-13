def countdown(x):
    while x >= 0:
        yield x
        x -= 1


for i in countdown(10):
    print(i)

print("-----------------------------------------")


def fibonacci(x):
    a = 0
    b = 1
    while b < x:
        yield b
        a, b = b, a + b


for i in fibonacci(10):
    print(i)

print("-----------------------------------------")


def calSqurd(x):
    a = 1
    while a < x:
        b = a ** 2
        yield a, b
        a += 1


for i, j in calSqurd(10):
    a = (i, j)
    print(a)

print("-----------------------------------------")
a01 = calSqurd(10)
