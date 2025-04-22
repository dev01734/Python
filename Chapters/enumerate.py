"""Enumerate Function : add counter to iterable and returns it"""

# l = [23,356,34,56,3]

# index=0
# for item in l:
#     print(f"The items nos at index {index} is {item}")
#     index += 1

# #Or can be done by enumerate

# for index, item in enumerate(l):
#     print(f"The items nos at index {index} is {item}")


"""List Comprehension : create list based on existing list"""
 
list = [3,8,4,6,7,9]

squaredlist =[]
for item in list:
    squaredlist.append(item*item)
print(squaredlist)

# Can be also written as

squaredlist = [i*i for i in list]
print(squaredlist)
    