'''Q1 to input name, marks & phone no of student and format it using format function 
like: "The name of student is Harry, his marks are 72 and phone no is 0920399092'''

# name=input("Enter Your Name Here : ")
# marks = int(input("Enter Your Marks Here : "))
# no = int(input("Enter Your Phone no Here : "))
# a = "The name of student is {}, his marks are {} and phone no is {}".format(name, marks, no)
# print(a)

'''Q2 list contains multiplication of 7. WAP to convert it to vertical string of
same no'''

# table =[str(7*i) for i in range(1,11)]
# s="\n".join(table)
# print(s)

'''Q3 filter list of nos divisible by 5'''
# l=[3,5,10,23,25,60,67]
# def divide(n):
#     if(n%5 == 0):
#         return True
#     return False
# onlyeven = filter(divide, l)
# print(list(onlyeven))

'''Q4 Find max of nos in list using reduce function'''
# from functools import reduce
# l= [1,3,3,5,8,4]
# def Max(a,b):
#     if (a>b):
#         return a
#     return b
# print(reduce(Max, l))

