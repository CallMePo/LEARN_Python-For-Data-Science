#exception akan terjadi ketika error pada runtime

#a = 1

#try:
#    b = int(input("Please enter a number to divide a"))
#    a = a / b
#   print("Success a=", a) #a>0
#except:
#    print("There was an error") #a=0
from numbers import Number
while(True):
    pembagian=int(input("Please enter a number to divide a"))
    try:
        divided=496734/pembagian
        print(f"result={divided}")
        is_done=input("next (y/n)?")
        if is_done == "n":
            break
    except:
        print("Divided by 0, enter the new number!")
print("the end")

while(True):
    try:
        with open("data.txt",'r') as file:
            print(file.read())
            break
    except:
        print("file doesn't exist, create the new file")
        with open("data.txt", 'w', encoding='utf-8') as file:
            file.write("Sesa")
        break
print("the END")

#create exception
def rules(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise "Input must be numbers"
    return a/b
print(rules(10,"o"))