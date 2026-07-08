class Car:
    def __init__(self,color):
        self._color=color

    def describe(self):
        return "This car is "+self._color


    def setColor(self,color):
        self._color=color

    @property
    def getColor(self):
        return self._color

redCar = Car('red')
print(redCar.describe())
redCar.setColor('blue')
print(redCar.getColor)

class Animal:
    def __init__(self,age):
        self._age=age
    @property
    def getAge(self):
        return self._age
    def speak(self):
        print("Make a Sound")

class Dog(Animal):
    def __init__(self,age,color):
        super().__init__(age)
        self._color=color
    def speak(self):
        print("Woof!!")
dog = Dog(12,"brown")
dog.speak()
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def print_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self._radius=radius
    def print_area(self):
        return self._radius*self._radius*3.14
class Rectangle(Shape):
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
    def print_area(self):
        return self._width*self._height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height


def area(Shape):
    return Shape.print_area()
circle = Circle(2)
print("Area: ",circle.print_area())

rectangle = Rectangle(2,3)
print("Width: ",rectangle.get_width())

import math
print("Square: ",math.sqrt(16))
print("The number Pi: ",math.pi)

print(dir(math))