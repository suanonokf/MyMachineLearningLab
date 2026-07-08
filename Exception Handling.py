
def division(number1,number2):
    try:
        return number1/number2
    except ZeroDivisionError:
        print("division by zero")
    except Exception:
        print("Use numbers only")

print(division("11",3))


file = open("test.txt",'r')
print(file.read())

with open("test.txt",'r') as file: # recommended way of handling file
    print(file.read())
# with open("number.txt",'w') as file:
#      file.write("1 2 3 4")

with open("number.txt") as file:
    sum=0;
    numbers=file.read().replace("\n","")
    for i in numbers:
        sum+=int(i)
    print(sum)

import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("File does not exist")