print(map(lambda x: x ** 2, [1, 2, 3, 4]))
print(map(lambda x, y: x + y, (1, 2, 3), [4, 5, 6]))

print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))

print(filter(lambda x: x % 2, [1, 2, 3, 4, 5]))
