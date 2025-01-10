import numpy as np
arr = np.array([[1, 2, 3, 4, 5],[3,4,5,2,1]])
print("NumPy Array:", arr)
print(arr.dtype)
print(arr.ndim)
print(arr.size)
print(arr.itemsize)
print(arr.shape)
for i in  arr.flat:
    print(i,end=' ')
n=np.zeros(5)
print(n) 
a=np.ones((2,4),dtype=int)
print(a)
b=np.full((2,3),12)   
print(b)
e=np.arange(1,10)
s=e*2
x=e**3
print(s)
print(x)
print(e)