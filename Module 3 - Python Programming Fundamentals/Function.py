#len()
#sum()

#sorted()#function
#i.sort()#method

album=[10,0.9,12,921.121,32]
album.sort()
#sortir=sorted(album)
#print(sortir)
print(album)

#Making function
def add1(a):
    b=a+1
    return b
print(add1(5))

#Multiple Parameter
def mult(f,g):
    d=f*g
    return d
print(mult("sesa ",2).split())

#loop in function
rate=[9, 8.12, 2.8, 7.4]
def haha(rate):
    for i,s in enumerate(rate):
        print("Rating",i,"is",s)

