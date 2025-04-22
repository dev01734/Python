'''Q1 WAP to open 3 file1.txt, file2.txt, file3.txt, if any of this is not present
then write a msg of not present and contine to code'''

# try:
#     with open ("file1.txt", 'r') as f:
#         print(f.read())
# except Exception as e:
#     print("File not found")

# try:
#     with open ("file2.txt", 'r') as f:
#         print(f.read())
# except Exception as e:
#     print("File not found")

# try:
#     with open ("file3.txt", 'r') as f:
#         print(f.read())
# except Exception as e:
#     print("File not found")

# print("Thanks")


'''Q2 Print 3rd, 5th and 7th element from list using enumerate'''

# l= [1,2,3,4,5,6,7,8]
# for i, item in enumerate(l):
#     if i == 2 or i==4 or i==6:
#         print(item)

'''Q3 list comprehension to print a list which contains multi table of user 
enter nos'''

# a= int(input("Enter a no: "))
# table = [a*i for i in range(1,11)]
# print(table)

'''Q4 display a/b where a & b are integers. If b=0 give zerodivision error'''

# a= int(input("Enter a no: "))
# b= int(input("Enter a no: "))
# try:
#     print(a/b)    
# except ZeroDivisionError:
#     print("Topa niche zero na ave")

# print("Jato re")

'''Q5 Store multiply table generated in Q3 in file name Tables.txt'''

a= int(input("Enter a no: "))
table = [a*i for i in range(1,11)]
with open ("Tables.txt", 'a') as f:
        f.write(str(table) + "\n")