''' Q1 class programmer to store info of programmer at Microsoft'''
# class Programmers:
#     company = "Microsoft"
#     def __init__(self, name, salary, language):  
#         self.name = name
#         self.salary= salary
#         self.language = language
#         print("I am a programmer at Microsoft")

# program= Programmers("raj", 5000000, "hindi")
# print(program.company, program.name, program.salary, program.language)
# rogram= Programmers("paj", 5000000, "hindi")
# print(rogram.company, rogram.name, rogram.salary, rogram.language)

''' Q2 class Calculator to get square/cube/square root of nos'''

# class Calc:
#     def __init__(self, n):
#         self.n = n 
#     def square(self):
#         print(f"the Square is : {self.n**2}")
#     def cube(self):
#         print(f"the cube is : {self.n**3}")
#     def squareroot(self):
#         print(f"the squareroot is : {self.n**0.5}")

# a = Calc(4)
# a.square()
# a.cube()
# a.squareroot()
'''ORRRRR'''
# class Calculator:
#     no = int(input("Enter nos You want ^2, ^3, ^1/2 of:  "))
#     print(f"Square of nos:{no**2}, Cube is : {no**3}, Square root is : {no**0.5}")


''' Q3 Create class attribute a; create an object from it and set 'a' directly 
using object a=0. Does it changes class attribute? No, an instance attribute is set and
class attribute is not changed'''

# class Demo:
#     a=4

# o=Demo()
# print(o.a)      # Prints class attribute as instance is not preset till now a=4
# o.a =0 
# print(o.a)      # now instance is presenst so it will print a=0
# print(Demo.a)   #prints class attribute

''' Q4 problem 2 with static and greet hello'''

# class Calc:
#     def __init__(self, n):
#         self.n = n 
#     def square(self):
#         print(f"the Square is : {self.n**2}")
#     def cube(self):
#         print(f"the cube is : {self.n**3}")
#     def squareroot(self):
#         print(f"the squareroot is : {self.n**0.5}")
#     @staticmethod
#     def greet():
#         print("good Morning")

# a = Calc(4)
# a.greet()
# a.square()
# a.cube()
# a.squareroot()

'''Q5 Class Train, method to book ticket, get status(no seats), get fare info'''

# from random import randint
# class Train:

#     def __init__(self, TrainNo):
#         self.TrainNo = TrainNo
#     def booking(self, fromm, to):
#         print(f"The train is booked: {self.TrainNo} from {fromm} to {to}")
#     def getStatus(self):
#         print(f"Train No: {self.TrainNo} & is running on time")
#     def getInfo(self, fromm, to):
#         print(f"The train info is: {self.TrainNo} from {fromm} to {to} is {randint(222,5555)}")

# t =Train (12334)
# t.booking("Ahmedabad", "Rajasthan")
# t.getStatus()
# t.getInfo("Ahmedabad", "Rajasthan")


''' Q6 can you change the self parameter inside a class to something else(say "harry")
.Try changing self to "slf" or "harry" and see effect? NO nothing will change but 
writing self is good practice'''

# class Train:

#     def __init__(harry, TrainNo):
#         harry.TrainNo = TrainNo
#     def booking(slf, fromm, to):
#         print(f"The train is booked: {slf.TrainNo} from {fromm} to {to}")
    
# t =Train (12334)
# t.booking("Ahmedabad", "Rajasthan")

