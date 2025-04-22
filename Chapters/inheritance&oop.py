"""In Inheritance: if we want methods of a class to be used in other class. Eg."""

# here in employee show method is used and we want to use same in Programmer
# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The name is {self.name}, salary is {self.salary}")

# class Programmer:
#     company = "ITC Info"
#     def show(self):
#         print(f"The name is {self.name}, salary is {self.salary}")
#     def showme(self):
#         print(f"The name is {self.name}, language is {self.language}")

# a= Employee()
# b= Programmer()
# print(a.company,b.company)

#That can be done like this 
'''(single inheritance)'''
# class Employee:                             #base class
#     company = "ITC"
#     def show(self, name, salary):
#         print(f"The name is {name}, salary is {salary}")

# class Programmer(Employee):         # all the methods of employee can now be used by programmer
#     company = "ITC Info"                # derived class
#     def showme(self,name, language):
#         print(f"The name is {name}, language is {language}")

# a= Employee()
# b= Programmer()
# a.show("raj", 2453656)
# b.showme("Raj", "JS")

"""3 types of inheritance: single(as done above), multiple(more than one base), 
multilevel()"""

#multiple inheritance
# class Employee:                            
#     salary = 142453426
#     name="raj"
#     def show(self):
#         print(f"The name is {self.name}, salary is {self.salary}")

# class Coder:        
#     language ="Python"
#     def printlang(self):
#         print(f"The language is {self.language}")

# class Programmer(Employee, Coder):        
#     company = "ITC Info"
#     def showme(self):
#         print(f"The name is {self.company}, language is {self.language}")

# a= Employee()
# b= Programmer()
# b.show()
# b.showme()
# b.printlang()


#multi level inheritance, parent has a child and that child also has a child
# class Employee:                            
#     a=1

# class Programmer(Employee):        
#     b=2

# class Manager(Programmer):        
#     c=3
# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)

'''Super Method : Used to access method(def) of super/parent class in derived class'''
# class Employee:    
#     def __init__(self):
#         print("cons of emp")                        
#     a=1

# class Programmer(Employee):        
#     def __init__(self):
#         print("cons of Prog")                        
#     b=2

# class Manager(Programmer):        
#     def __init__(self):
#         super().__init__()      # due to this cons of Prog  & cons of Man will run
#         print("cons of Man")                        
#     c=3
# o = Employee()  # here only "cons of emp" will work
# print(o.a)

# o = Programmer()# here only "cons of Prog" will work but we also want to run "cons of emp" we use super
# print(o.a, o.b)

# o = Manager()   # here only "cons of Man" will work but we also want to run "cons of prog" we use super
# print(o.a, o.b, o.c)

'''Class Method: Method which is bound to the class and not an object, to access class inside a method,
so it is used if we dont want class to be updated by instance''' 

# class Employee:     #not used class method, so class will be updated by instance and print 45 instead of 1 
#     a=1
#     def show(cls):
#         print(f"The value of class attribute is, {cls.a}")
# e=Employee()
# e.a=45
# e.show()

# class Employee1:   #used class method, so class will not be updated by and print even if instance is provided
#     b=1
#     @classmethod
#     def show(cls):
#         print(f"The value of class attribute is, {cls.b}")
# e=Employee1()
# e.b=45
# e.show()

'''Property Decorators: '''

# class Employee1:  
#     @classmethod
#     def show(cls):
#         print(f"The value of class attribute is, {cls.b}")
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]
# e=Employee1()
# e.name="Haryy Laal"
# print(e.name)
# print(e.fname, e.lname)

"""This is called Encapsulation and Abstraction
Encapsulation: so many components are packed in one unit as here is a class Employee1
Abstraction: Implementation details are hidden from user"""

'''Operator Overloading'''
class Number:
    def __init__(self, a, b):
        self.n =n
    def __add__(self, num):             #are given when used with objects, direct + will not work
        return self.n + num.n
    def __str__(self):
        return self.Raj
a=Number
n= Number(1)
m= Number(2)
print(n+m)

a.self="dev"
print(a.self)

'''Egs. __add__, __sub__, __mul__, __truediv__, __floordiv__, __str__, __len__'''