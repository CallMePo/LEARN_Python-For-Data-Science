import numpy as np
import matplotlib.pyplot as plt

 #The basic and Array creation
a=np.array([1,3,4,2,32,67])
print(type(a))
print(a.dtype)
print(a[3])
print(a.size)
print(a.ndim) #represent the number of array dimensions or the rank of the array
print(a.shape) #is a tuple of integers indicating the size of the array in each dimension

 #Indexing and slicing
b=np.array([684,13,763,2141,129,9,18,45])
b[0]=1
print(b)
c=b[2:5]
print(c)

 #Basic operations
    #Vector addition & Substraction
u2=[1,0]
v2=[1,0]
z2=[]
for n,m in zip(u2,v2):
    z2.append(n+m)
print(z2)

u1=np.array([1,0])
v1=np.array([0,1])
z1=u1+v1
print(z1)

    #Array multiplication with a scalar
s=[2,9]
r=[]
for n in s:
    r.append(2*n)
print(r)

se=np.array([3,1])
ra=2*se
print(ra)

    #Product of two numpy arrays
u=[3, 8]
v=[2, 4]
z=[]
for n,m in zip(u,v):
    z.append(n*m)
print(z)

e=np.array([6,1])
h=np.array([2,9])
l=e*h
print(l)

    #Dot product
p=np.array([23,2])
g=np.array([1,8])
result=np.dot(p,g) #(23 x 1) + (2 x 8)
print(result, "ini dot")

    #Adding constant to an numpy array
t=np.array([0,2,3,4,5,-1])
d=t+1
print(d)

j=[2,35,-12,31,]
k=[]
for n in j:
    k.append(n-3)
print(k)

 #Universal functions
ad=np.array([1,-1,1,2])
rata=ad.mean()
max=ad.max()
print(rata)
print(max)

x=np.array([0, np.pi/2, np.pi])
y1=np.sin(x)
print(y1)

    #Plotting Mathematical functions
#
#note=np.linspace(-2,2, num=9) #index start from -2 to 2, the num=9 represent there are 9 index or 9 spaces (have to)

b=np.linspace(0,2*np.pi, 100)
nb=np.sin(b)

plt.plot(b,nb)
