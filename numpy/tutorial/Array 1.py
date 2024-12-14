import numpy as np

a=np.array([2,11,53])
print(a)
print(a[1])
#a[start:stop:step] | slice array 1 มิติ
print(a[:1:2])

b=np.array([[1,2],[3,4],[5,6]])
print(b)
#b[row][col]
print(b[1][0])
#b[start:stop:step,start:stop:step] | b[row,col] | slice array 2 มิติ
print(b[1:2,1:2])

c=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(c)
#c[dept][row][col]
print(c[1][0][1])

d=np.array([[1,2,3]],dtype="str")
print(d)

# Attribute numpy
print(b.shape)
print(b.size)

#index
index = np.array([2])
print(a[index])
print(b[[0,1],[1,1]])