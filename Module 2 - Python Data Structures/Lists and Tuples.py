#Tuples
tuple1=(10, "sesa", 3.6)
print(tuple1[1])
tuple2=tuple1 + ("cantik", 100.9, 99)
print(tuple2)
#Tuple: slicing
print(tuple2[0:4])
print(len(tuple2))
#Tuple: immutable
tuple3=(11, 993.019,-113,-139821.2232)
print(sorted(tuple3))
#Tuple: nesting
tuple4=(1,2,("Sesa","Dimitri"),3.2)
print(len(tuple4))
print(tuple4[2])
print(tuple4[2][1])

#Lists
List = ["Sesa",10, 9.2]
print(List[0:2])
Lists = List + ["Shadiim"]
print(Lists)

List.extend(Lists)
print(List)

List.append(Lists)
print(List)

del(List[1])
print(List)

#Convert string to list
masaDepan="Shafaa Dimitri Azalea".split()
print(masaDepan)
namaMama ="sesa, shafa, shadim".split(",")
print(namaMama)

#List: aliasing
A=["Azalea"]
B=["Sesaa"]
B = A
print(B[0])

#List: clone
B=A[:]
print(B)
