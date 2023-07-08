# len()
# sum()

# sorted()#function
# i.sort()#method

album = [10, 0.9, 12, 921.121, 32]
album.sort()
# sortir=sorted(album)
# print(sortir)
print(album)


# Making function
def add1(a):
    b = a + 1
    return b


print(add1(5))


# Multiple Parameter
def mult(f, g):
    d = f * g
    return d


print(mult("sesa ", 2).split())

# loop in function
rate = [9, 8.12, 2.8, 7.4]


def haha(rate):
    for i, s in enumerate(rate):
        print("Rating", i, "is", s)


album_rate = [10, 8.5, 9.5]
haha(album_rate)


# Scope: global
def artisname(*names):
    for name in names:
        print(name)


artisname("Shafaa", "Sesa")


def AddDC(x):
    x = x + "DC"
    print(x)
    return (x)


x = "AC"
z = AddDC(x)


# Scope: local
def thriller():
    Date = 2022
    return (Date)


Date = 2017

print(thriller())
print(Date)


# Scope: variables
def acdc(y):
    print(Rating)
    return (Rating)


Rating = 9
Z = acdc(1)
print(Rating)


# Scope: local variabels
def sesa():
    global claimedWife
    claimedWife = 'atrk'
    return claimedWife


sesa()
print(sesa())


# LAB
def g(c):
    return sum(c)


c = [1, 2, 3, 4, 5]

if sum(c) == g(c):
    print("Correct.")
else:
    print("Incorrect.")
