''' Q1 get 4 user nos and find which is greatest'''
# nos1=int(input("Enter any no: "))
# nos2=int(input("Enter any no: "))
# nos3=int(input("Enter any no: "))
# nos4=int(input("Enter any no: "))
# if(nos1 > nos2 and nos1 >nos3 and nos1 > nos4):  
#     print("nos1 is greatest")
# elif(nos2 > nos1 and nos2 >nos3 and nos2 >nos4):
#     print("nos2 is greatest")
# elif(nos3 > nos1 and nos3 >nos2 and nos3 >nos4):
#     print("nos3 is greatest")
# else:
#     print("nos4 is greatest")

'''Q2 get 3 marks from user and find if he passed of failed 40%min and 33%min in each'''
# s1= int(input("Enter marks of subject1: "))
# s2= int(input("Enter marks of subject2: "))
# s3= int(input("Enter marks of subject3: "))
# a=(((s1+s2+s3)/300))*100
# if(a>=40 and s1>=33 and s2>=33 and s3>=33):
#     print("passed",a, s1, s2, s3)
# else:
#     print("failed",a, s1, s2, s3)


'''Q3 if msg contains this keyword it is considered as spam'''
# a=("Make Money")
# b=( buy now")
# c=("sub")
# d=("click here")
# comment=(input("enter the comment: "))
# if(a in comment or b in comment or c in comment or d in comment):
#     print("its a spam")
# else:
#     print("not spam")

'''Q4 program to give username contains character length 10 or not'''
# username=input("Enter your username: ")
# if(len(username)<10):
#     print("its small")
# else:
#     print("its big")


'''Q5 Find if name is present in a List or not'''
# list=["dev", "raj", "ds", "har"]
# name= input("Enter your name here : ")
# if(name in list):
#     print("You are present")
# else:
#     print("Not today")

'''Q6 calc grade of student in this scheme'''
# marks=int(input("enter your marks here:"))
# if(marks >90 and marks <=100):
#     print("you are excellent")
# elif(marks >80 and marks <90):
#     print("A grade")
# elif(marks >70 and marks <80):
#     print("B grade")
# elif(marks >60 and marks <70):
#     print("C grade")
# elif(marks >50 and marks <60):
#     print("D grade")
# elif(marks < 50):
#     print("failed")

'''Q7 find out if this is talking about dev'''
# post = input("Enter your post here: ")
# if("dev".lower() in post.lower()):          
'''.lower() will convert all input into lower case so if we write dev/Dev/dEv anything it will be 
converted to lower and as we are talking about dev it will be found'''
#     print("Post is talking about dev")
# else:
#     print("Post is not talking about dev")


