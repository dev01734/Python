'''Dictionary'''
# d= {} #it creates an empty dictionary
# s= set() # it creates an empty set, cant repeat values in a set 

# marks = {
#     "American Express" : 1041101343,
#     "BOB" : 9860983576,
#     "HDFC": 48756425,
#     134546 : "BOB"
# }
# print(marks.get("BOBY"))              #Print none
# print(marks["BOBY"])                  #gives an error if that key is not found


'''Sets'''
#1 there is a prebuild dictionary and user will enter a hindi word and
# output will be english value of it
# words= {
#         "madad":"help",
#         "billi":"cat"
#         }
# word=input("enter word you want a meaning of: ")
# print(words[word])

#2 let user enter 4 nos and all will be unique
# s=set()
# d=input("enter nos 1: ")
# s.add(int(d))
# d=input("enter nos 2: ")
# s.add(int(d))
# d=input("enter nos 3: ")
# s.add(int(d))
# d=input("enter nos 4: ")
# s.add(int(d))
# d=input("enter nos 5: ")
# s.add(int(d))
# d=input("enter nos 6: ")
# s.add(int(d))
# d=input("enter nos 7: ")
# s.add(int(d))
# d=input("enter nos 8: ")
# s.add(int(d))
# print(s)

# 3 are 18 & 18.0 considered as same value or not?
# s=set()
# s.add(18)
# s.add(18.0)  #18 and 18.0 are considered as same values
# s.add('18')
# print(len(s))

# 4 let user enter 4 name and 4 languages in a dictionary
# movies={}
# name=input("friends name: ")
# lan=input("input lang name: ")
# movies.update({name: lan})
# name=input("friends name: ")
# lan=input("input lang name: ")
# movies.update({name: lan})
# name=input("friends name: ")
# lan=input("input lang name: ")
# movies.update({name: lan})
# name=input("friends name: ")
# lan=input("input lang name: ")
# movies.update({name: lan})
# print(movies)

#5 Can you change the values in a list present in a Set
# s={1,2,43, "Har",[3,4]} # you cant change that list value, & sets are immutable
