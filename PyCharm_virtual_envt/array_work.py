import numpy as np

a = np.linspace(1,3,10)
print(a)

a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a.sum()) # sum of array
print(a.max())# print max value
print(a.min())# print min value

b = np.array([(1,2,3),(3,4,5)])
print(b.sum(axis=0))
print(b.sum(axis=1))

print(np.sqrt(b)) # suare root
print(np.sqrt(a)) # suare root
