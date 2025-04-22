"""Functions used when code gets large and want to smaller it Example: """

# def avg():
#     a=int(input("Enter your nos here: "))
#     b=int(input("Enter your nos here: "))
#     c=int(input("Enter your nos here: "))
#     av= (a+b+c)/3
#     print(av)

# avg()   #used to call that function

"""Two types of Functions : Built in Functions & User Defined"""

'''Default Argument'''
# def Goodday(name, ending="Thank You"):
#     print(f"Goodday, {name}")
#     print(ending)                   # ending in def is given default argument and it will 
#                                                                 # printed as it is
# Goodday("dev")


''' Q1 use Functions to find greatest nos of all three'''
# def greatest(a, b, c):
#     # a=int(input("enter your here:"))   #This 3 input can be used or below  a/b/c are used /
#     # b=int(input("enter your here:"))
#     # c=int(input("enter your here:"))
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c

# a=1
# b=2
# c=6
# print(greatest(a,b,c))


''' Q2 convert Celsius to Fahrenheit'''
# def CtoF(c):
#       return((c/5)*9)+32

# c=int(input("Enter Temp in Celsius here: "))
# print(CtoF(c))
        
''' Q3 How to prevent python print() function to print new line in end'''
# print("a")
# print("b")
# print("c", end="")
# print("d", end="")

'''Q4 print a pattern'''
# def pattern(n):
#     if(n==0):
#         return    #code will not run ahead as return is seen
#     print("*" * n)
#     pattern(n-1)

# pattern(3)

'''Q5 Convert inches to cms'''
# def inch_to_cms(inch):
#     if(inch==0):
#         return
#     return 2.54*inch
# i=int(input("Enter value in inches : "))
# print(f"Inches to centimeter is, {inch_to_cms(i)}")

''' Q6 remove a word from a list and strip it at the same time'''
# def rem(l, word):
#     n=[]
#     for item in l:
#         if (item!=word):
#             n.append(item.strip(word))
#     return n

# l=["Harry", "Shubham", "Rohan", "an"]
# print(rem(l, "an"))

''' Q7 Print multiplication table of given func'''
# def mul():
#     i=int(input("Enter no you want to multiply: "))
#     for mul in range(1, 11):
#         print(f"{i} X {mul} = {i*mul}")
# mul()

"""OR"""
def mul(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {i*n}")

mul(5)