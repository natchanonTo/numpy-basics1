import numpy as np

#empty
a = np.empty([5,5])
print(a)

#identity
b = np.identity(6,dtype="int")
print(b)

#eye
c = np.eye(4)
print(c)
d = np.eye(4,5)
print(d)
e = np.eye(3,6,k=1)
print(e)
f = np.eye(3,k=-1)
print(f)