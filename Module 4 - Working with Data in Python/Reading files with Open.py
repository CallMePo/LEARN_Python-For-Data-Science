with open("example.txt",'w') as file:# 'w' for write, 'r' for read
    file_stuff=file.write("Shafaa Dimitri Azalea\n Shadim\n sesa\n dimdim")
with open("example.txt", 'r')as file2:
    file_stuff2=file2.read()
    print(file_stuff2)
with open("example.txt", 'r') as file:
    fileku=file.readlines()
    print(fileku)

#Download data
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url,filename)

#Read data
with open("Example1.txt",'r') as files:
    data=files.readlines()
    print(data[2])