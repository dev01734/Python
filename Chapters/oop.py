"""Normal class attribute and instance attribute"""
# class Owner: 
#     lan ="english"                  # this is a class attribute
#     Net_Profit =70000000

# #here name is instance(object) attribute and salary/language are class attribute as they belong to class

# dev = Owner()
# dev.name= "Devansh"                   # this is a Instance/object attribute
# print(f"name  : {dev.name}\nNet Profit : {dev.Net_Profit}")

# dev = Owner()
# dev.name= "Dev"
# print(f"name  : {dev.name}\nNet Profit : {dev.Net_Profit}")

"""Instance attribute has higher preference than class"""
# class Employee:
#     language = "English"
#     salary = 500000

# emp = Employee()
# emp.language = "Hindi"                        #has more preference 
# print(emp.language, emp.salary)

"""Self Parameter"""

# class Employee:
#     language = "English"
#     salary = 500000
     
#     def getInfo(self):
#         print(f"The lang is {self.language}, salary is {self.salary}, Good Morning!")

# harry = Employee()

# harry.getInfo()  
# # equivalent to 'Employee.getInfo(harry)'


'''Static Method'''
# class Employee:
#     language = "English"
#     salary = 500000
     
#     def getInfo(self):
#         print(f"The lang is {self.language}, salary is {self.salary}")
    
#     @staticmethod               # no need to give object like 'self' as given above
#     def greet():
#         print("Good Morning!")

# harry = Employee()

# harry.getInfo()  
# harry.greet()

'''__init__() constructor : which is dunder method which will be called itself as class is called'''

class Employee:
    language = "English"
    salary = 500000

    def __init__(self, name, salary, lanuage):  #__init__ is a dunder method which is auto called
        self.name = name
        self.salary= salary
        self.language = lanuage
        print("I am creating an object")
     
    def getInfo(self):
        print(f"The lang is {self.language}, salary is {self.salary}, Good Morning!")

harry = Employee("raj", 5000000, "Gujarati")
print(harry.name, harry.language, harry.salary)
