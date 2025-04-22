"""Used to let user know that he has entered something wrong"""
#Eg. :If he will enter a number, it will be printed but if he input a str, 
# float then insted of code crash it will give output as wrong input

'''Try input a no. and again try input a str/float'''
# try:
#     a = int(input("Enter a Nos: "))
#     print(a)
# except Exception as e:
#     print(e)
# print("Thank You")

'''We can also throw particular type of error'''
# try:
#     a = int(input("Enter a Nos: "))
#     print(a)
# except ZeroDivisionError as v:
#     print("Topa")
#     print(v)
# except ValueError as c:
#     print("Gadheda")
#     print(c)
# except Exception as e:
#     print(e)
# print("Thank You")
    
'''Raising Exceptions'''

# a = int(input("Enter a Nos: "))
# b = int(input("Enter second Nos: "))
# if (b==0):
#     raise ZeroDivisionError("Topa niche kadi zero na ve")
# else:
#     print(f"The answer is {a/b}")

'''Try with else Clause : else will only run when try will be done, if except will run then else will not 
work, we want to run a code when try is success'''

# try:
#     a = int(input("Enter a Nos: "))
#     print(a)
# except Exception as v:
#     print(v)
# else:           #runs only when try will be executed
#     print("im inside else")

'''Try with finally: finally block will run anyhow, in try and in except.Its mainly used in function.
If in function we don't write finally that print will not run. Eg. Given'''

# def main():
#     try:
#         a = int(input("Enter a Nos: "))
#         print(a)
#         return
#     except Exception as v:
#         print(v)
#         return
#     finally:
#         print("im inside finally")
# main()

#here print("im inside finally") will not run

# def main():
#     try:
#         a = int(input("Enter a Nos: "))
#         print(a)
#         return
#     except Exception as v:
#         print(v)
#         return
#     print("im inside finally")
# main()

'''if __NAME__ == "MAIN" : in nameamin1.py and module.py '''