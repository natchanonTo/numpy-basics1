import numpy as np

a = np.arange(1,10)
print(a)

print(a.sum())
print(a.prod())
print(a.mean())
print(a.max())
print(a.min())
print(a.argmax())
print(a.argmin())

b = np.array([[10,20,30],[40,50,60],[70,100,2]])
print(b)

print(np.min(b,axis=1))
print(np.min(b,axis=0))
print(np.max(b,axis=0))
print(np.max(b,axis=1))