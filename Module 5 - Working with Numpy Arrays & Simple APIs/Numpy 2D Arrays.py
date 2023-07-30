import numpy as np

a=[[11,12,13],[21,22,23],[31,32,33]]
b=[[41,42,43],[51,52,53],[61,62,63]]
A=np.array(a)
B=np.array(b)
print(A)
print(A.ndim)
print(A.shape)
print(A.size)
print(A[2][1])
print(A[0:2,2])
print(A+B) #index A0 + B0 such like that
print(2*A) #each index multiply w/ value 2

c=[[1,2,3],[11,22,33]]
d=[[10,11],[20,21],[30,31]]
C=np.array(c)
print(C, "ini C")
D=np.array(d)
print(D, "ini D")
#print(C*D)
print(np.dot(C,D))