with open("example.txt",'w') as file:# 'w' for write, 'r' for read
    file_stuff=file.write("Shafaa Dimitri Azalea \nShadim")
with open("example.txt", 'r')as file2:
    file_stuff2=file2.read()
    print(file_stuff2)
with open("example.txt", 'r') as file:
    fileku=file.readlines(1)
    print(fileku)