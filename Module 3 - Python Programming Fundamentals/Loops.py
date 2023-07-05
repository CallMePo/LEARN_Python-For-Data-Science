#RANGE
# range(3)==[0,1,2]
# range(10, 15)==[10,12,13,14]

#for loops
kotak=["red","yellow","green","purple","blue"]
for i in range(0,5):
    kotak[i]="white"
print(kotak)

#while loops
istri=["sesa","sesa","sesa","shafaa","shadim"]
istriReal=[]
i=0 #start at index 0
while(istri[i]=="sesa"):
    istriReal.append(istri[i])
    i=i+1
print(istriReal)

x=2
y=1
while(y!=x):
     print(y)
y=y+1
#kode tersebut akan mencetak nilai y secara berulang sampai nilai y sama dengan nilai x. Jika x sama dengan 2 dan y sama dengan 1, maka kode akan mencetak nilai 1. Kemudian, nilai y akan ditambahkan 1 sehingga menjadi 2, dan karena kondisi y!=x tidak terpenuhi, perulangan while akan berhenti.