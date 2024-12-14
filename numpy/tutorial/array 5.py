import numpy as np

a = np.arange(1,21)
a = a.reshape(5,4)

b = np.hsplit(a,4)

print(a)
print(b)

c = np.vsplit(a,5)

print(c)