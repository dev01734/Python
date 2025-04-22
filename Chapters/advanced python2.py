"""Venv : virtual Environment : 
    1 pip install virtualenv
    2 virtualenv environment""" #here environment is name of virtual environment

'''How to activate that virtual environment : 
which can be used to when we need different versions of a library,
its same as interpreter but is isolated from other python environments on system'''
#1 after this two steps a new folder will be created
#2 to activate it we write .\env\Scripts\activate\ps1
#3 packages installed in that virtual environment by : pip freeze, pip freeze > requirements.txt to save all that packages in a requirement.txt


#3 to deactivate it write, deactivate


#pip install -r .\requirements.txt , to install all those packages to other env or pc


"""Lambda Functions : A easier way to create a function in form of expression"""
#Eg.

# def square(n):
#     return n*n
# print(square(5))

#Or

# square=lambda s:s*s
# print(square(5))


"""Join Method : Works only for string, to join values"""

# list=["har", "adf", "eew"]
# l = "::".join(list)
# print(l)

# a = ("ef", "efe","wrgt")
# d = "-".join(a)
# print(d)


""" Format Method : Not used now """
# a= "{} is a good {}".format("harry", "boy")
# print(a)

# # works like
# a= "{0} is a good {1}".format("harry", "boy")
# print(a)


"""Map, Filter, Reduce"""
#Map : applies a function to all items in an inputlist

# l= [1,3,3,5,8,4]
# square = lambda x:x*x
# sqlist = map(square, l)           # map(function->(square), input list->(l))
# print(list(sqlist))

#Filter : Returns that only valuesfo which function is True
# l= [1,3,3,5,8,4]
# def Even(n):
#     if(n%2 ==0):
#         return True
#     return False
# onlyeven = filter(Even, l)
# print(list(onlyeven))

#Reduce : Applies sequential computation to pair of elements, need to import fro functools
#Eg 1,3,3,5,8,4 = 1 + 3 = 4 + 3 = 7 + 5 = 12 + 8 = 20 + 4 = 24

# from functools import reduce
# l= [1,3,3,5,8,4]

# def Sum(a,b):
#     return a+b
# print(reduce(Sum, l)) 
# #        OR         #
# sum = lambda x,y : x+y
# print(reduce(sum, l))