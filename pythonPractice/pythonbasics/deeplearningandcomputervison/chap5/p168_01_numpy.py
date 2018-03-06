import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = np.array(a)
print(type(b))
print(b.shape)
print(b.argmax())
print(b.max())
print(b.mean())
