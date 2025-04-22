"""Recursion is a Function that calls itself, for math functions"""
'''factorial(n) = n * factorial(n-1)'''
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)        # calls itself

# n= int(input("Enter no here: "))
# print(f"Factorial of n is: {factorial(n)}")

'''Q1 Recursive funtion to calc sum of first n natural nos'''
# def sum(s):
#     if(s==1):
#         return  1
#     if(s==0):
#         return  0
#     return s + sum(s-1)
# s= int(input("Enter no here: "))
# print(f"Sum of n natural no is {sum(s)}")