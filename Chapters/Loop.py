'''For Loop can be done with list, tuples and also string'''
# for i in range (1, 6):
#     print(i)

'''For loop with else'''
# l=[123,235,43,56]
# for item in l:
#     print(item)
# else:
#     print("Done")

'''For loop with break/Continue/Pass; to come out of the loop'''
# for i in range(100):
#     if(i == 34):
#         break # will exit the loop
#     print(i)


# for i in range(100):
#     if(i == 34):
#         continue # will skip that iteration from the loop
#     print(i)


# for i in range(100):
#         pass # does nothing to the loop, it will not run for loop and directly runs while loop
# while(i<45):
#     print(i)
#     i+=1


'''While Loop'''
# l=[134, True, "dev", "raj", "123"]
# i = 0
# while(i<len(l)):
#     print(l[i])
#     i +=1    

''' Q1 give multiplication table in for loop of given nos'''
# nos= int(input("enter your nos here: "))
# i=1
# for i in range (1,11):
#     print(f"{nos} X {i} = {nos*i}")

''' Q2 Greet all person name from list whose name starts with S'''
# Names=["Dev", "Soham", "sundar", "Manus"]
# for Name in Names:
#     if(Name.startswith("S")):
#         print(f"you are in {Name}")

''' Q3 1st question using while loop'''
# nos = int(input("Enter your nos here: "))
# i=1
# while(i<=10 and nos*1):
#     print(f"{nos} X {i} = {nos*i}")
#     i+=1

''' Q4 find whether a nos is prime or not '''
# nos = int(input("Enter your nos here: "))
# for i in range(2,nos):
#     if(nos%i)==0:
#         print("nos is not prime")
#         break
# else:
#  print("nos is prime")

''' Q5 using while get sum of n natural nos'''
# nos = int(input("Enter your nos here: "))
# i=1
# sum=0
# while(i<=nos):
#     sum+=i
#     i+=1
# print(sum)

''' Q6 Factorial of give nos in for loop'''
# nos = int(input("Enter your nos here: "))
# mul=1
# for i in range(1,nos+1):
#     mul= mul*i
# print(f"the factorial of nos given is: {mul}" )

''' Q7 to create a star pattern'''
# n = int(input("Enter your nos here: "))
# for i in range(1 ,n+1):
#     print(" " * (n-i), end="") # end() doesnt add a new line itself
#     print("*" * (2*i-1), end="") #2*i-1 is used to print odd values
#     print("")

# n = int(input("Enter your nos here: "))
# for i in range(1 ,n+1):
#     print("*" * i, end="") #2*i-1 is used to print odd values
#     print("")

# n = int(input("Enter your nos here: "))
# for i in range(1 ,n+1):
#     if(i==1 or i==n):
#         print("*" * n,end="")
#     else:
#         print("*",end="")
#         print(" " * (n-2),end="")
#         print("*",end="")
#     print("")

''' Q10 print multi table of n using loop in reverse'''
n = int(input("Enter nos you want to multiply here: "))
i=1
for i in range(1,11):
   print(f"{n} X {11-i} = {n*(11-i)}")
