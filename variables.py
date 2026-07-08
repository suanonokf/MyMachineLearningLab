name ="fadil"
print("Your name is: ",name)

num1 = 12
num2 =13
print("Total is: ",num1+num2)

# age=input("What is your age?")
# print("Your age is: ",age)

aStringNumber = "123"
convertStringNumber = int(aStringNumber)
print(convertStringNumber,"Type: ",type(convertStringNumber))

price= 19.99
convertInInt = int(price)
print(convertInInt,"Type: ",type(convertInInt))

#multi line string
text=("A text on line 1\n"
      "A text on line 2\n"
       "A text on line 3\n")
print(text)

message ="I'm learning python programming"
print("If contains: ",message.__contains__("python"))

aNumber = 54
if(aNumber>=1 and aNumber<=100):
    print(aNumber," is on the set")

isTrue = True
reverse = not isTrue
print(reverse)

list1 =[1,2,3]
list2 = [1,2,3]
print(list1 == list2)

if(1 in list1):
    print("1 is in the list")

aString = "hello"
for i in aString:
    print(i)

list3 = [1,2,3,4,5]
total=0;
for i in list3:
    total=total+i
print(total)

num=1
while num<=5:
    print(num)
    num=num+1

for i in range(3):
    for j in range(3):
        print("*",end="")
    print()

def greet():
    print("Hello")
greet()

def square(x):
    return x*x;
print("Square: ",square(4))

def function():
    aVariable="Variable"
def greeting(name,message="Hello"):
    print(message,name)

print(greeting("Karl"))

multiply = lambda num1,num2: num1*num2
print(multiply(5,2))

aList = [1,2,3,4,5,6,7,8,9]
evenNumber=filter(lambda num: num%2==0,aList)
print(list(evenNumber))
squareNumber = map(lambda x: x*x,aList)
print(list(squareNumber))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
#Data structures
fruits = ["apple","banana","orange"] # a list is mutable and uses [] while a tuple is immutable and uses ()
print(fruits[1])
fruits.append("cherry")

dictionnary={
    "name":"Karl",
    "age":18,
    "city":"Abidjan"
}
keys=dictionnary.keys()
print("Keys: ",keys)
values=dictionnary.values()
print("Values: ",values)
print(dictionnary)
fruits.pop()
print(fruits)

duplicateElemnts=[1,2,3,3,1,7,8,9,6,6,4,5,6,7,8,9]
print(set(duplicateElemnts))