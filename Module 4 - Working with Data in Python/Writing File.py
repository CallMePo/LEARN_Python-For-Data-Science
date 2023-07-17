Nama=["Sesa\n","Sesi\n","Shafaa\n"]
with open("Shafaa dim dim.txt", 'w') as file_nama:
    for line in Nama:
        file_nama.write(line)

with open("Shafaa dim dim.txt", 'r') as baca:
    #membaca=baca.read()
    #print(membaca)
    with open("sesayang.txt",'w') as future:
        for line in baca:
            future.write(line)
    print(future.read())

#Additional modes
#r+ : Reading and writing. Cannot truncate the file.
#w+ : Writing and reading. Truncates the file.
#a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.

with open("sesayang.txt",'a+') as hehe:
    hehe.write("Shafaa Dimitri Azalea\n")
    hehe.seek(0)
    print(hehe.read())