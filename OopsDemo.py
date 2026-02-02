# Classes are user defined blueprint or prototype
# Classes can have methods , class variables , instance variables, construtor etc..
# SELF KEYWORD IS MANDATORY FOR CALLING VARIABLE NAMES INTO METHOD

class Calculator:
    # num = 100 # class variables and will be constant no matter how many objects we create
    # default constructor

    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("Automatically called when object is created")

    def getData (self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber


obj = Calculator(2, 3) # syntax to create objects in python
obj.getData()
print(obj.summation())

obj1 = Calculator(5, 6)
obj1.getData()
print(obj1.summation())

obj2 = Calculator(500, 600)
obj2.getData()
print(obj2.summation())