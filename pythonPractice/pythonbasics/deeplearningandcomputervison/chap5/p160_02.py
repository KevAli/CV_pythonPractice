def get_val_at_pos_1(x):
    return x[1]


heroes = {
    ('Superman', 99, 666),
    ('Batman', 100, 777),
    ('Joker', 85, 888),
    ('Ali', 90, 999)
}
sorted_pairs0 = sorted(heroes, key=get_val_at_pos_1)
sorted_pairs1 = sorted(heroes, key=lambda x: (x[1] + x[2]) / 2)
print(sorted_pairs0)
print(sorted_pairs1)

some_ops = lambda x, y: x + y + x * y + x ** y
print(some_ops(2, 3))
