import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7])
c = np.array([8, 9, 10, 11, 12])
p, q, r = np.ix_(a, b, c)
print(p)