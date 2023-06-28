#dictionary is like list but the index is has value. the value not must be integers, and also unique,immutable
masaDepan={"Shafaa":2003, "Sesa":2004, "Dimitri":2005}
print(masaDepan["Shafaa"])
masaDepan["Shadim"]="2006"
print(masaDepan)
print("starboy" in masaDepan)

print(masaDepan.values())

#TEST
D = {'a':0,'b':1,'c':2} #what is result of the following: D.values() ?
print(D.values())

D = {'a':0,'b':1,'c':2} #what is the output of D['b']?
print(D['b'])
