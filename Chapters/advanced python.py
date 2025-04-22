"""Walrus Operator(:=) allows to assign values to variable parts of expression."""
#Eg.

# if(n := len([1,2,3,5,4])) > 3:
#     print(f"List is too long ({n} elements, expected <=3)")

#instead of 

# n = len([1,2,3,4,5])
# if (n>3):
#     print(f"List is too long ({n} elements, expected <=3)")

#this both codes are same but 1st uses Walrus operator to shorten its length

"""Type Definations in Python : To know the code easily, that which function 
return what"""
#Eg.
# a : int = 5           # represented like this: 
# b : str ="rta"        # we give the types of variables and function

# def sum(a : int, b : int) -> int:       # like is it str, int, float
#     return a+b

# print(sum(4,5))


"""Advanced Type Hints : from typing module"""
#Eg

# from typing import List, Tuple, Dict, Union
# n : List[int] = [1,2,4,5,6]
# a : Tuple[str, int] = ["rafg", 234]
# b : Dict[str:int] = {"raj" : 14, "usg" : 235}
# # union can hold multiple datatype as both of below are valid
# u : Union[int, str] = "IFHD"
# u = 3545


"""Match Case : Similar to switch statement """

# def https_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Status"
# print(https_status(200))
# print(https_status(404))
# print(https_status(500))
# print(https_status(403))


"""Dictionay Merge : Merge two dicts"""

# dict1 = {"deer" :34, "wdf" : 34}
# dict2=  {"dr" :3234, "wdds" : 134}
# merge = dict1 | dict2
# print(merge)


"""Now can use multiple Context manager in single 'with' statement"""

# with(
#     open('file.txt') as f1,
#     open('file1.txt') as f2
# ):

