import numpy as np

a = np.ones((10, 10), dtype=np.float)
b = np.zeros((10, 10))

c = 1
for i in range(10):
    for j in range(10):
        a[i, j] = c
        c += 1

print(a)

print(a[0:3, 0:3])
print('------------------------')
print(a[0:3, -3:])
print('------------------------')
print(a[-3:, -3:])
print('------------------------')
print(a[-3:, 0:3])
