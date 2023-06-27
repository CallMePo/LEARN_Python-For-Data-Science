set1={"sesa","shadim","azalea","sesa","shafa"}
print(set1)

#Convert from list to set
namaMama=["sesa","shafa","shadim","sesa"]
print(set(namaMama))

#Set operation
set1.add("sesayang")
print(set1)

set1.remove("azalea")
print(set1)

#Set: mathematical ooperation
set1={"sesa","shadim","azalea","sesa","shafa"}
set2={"sesa","shadim","azalea","sesa","shafa","sesayang"}
set3=set2&set1
print(set3)

set4=set1.union(set2)
print(set4)

set5=set1.issubset(set2)
print(set5)