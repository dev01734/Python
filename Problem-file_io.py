''' Q1 read text from a file and find if it has happy word in it'''

# with open("file.txt") as f:
#     file= f.read()
#     if("Happy" in file):
#         print("found it")
'''Or'''
# f=open("file.txt")
# line=f.read()
# if("Happy" in line):
#     print("Found It", )
# else:
#     print("not found")
# f.close()

''' Q2 game()function and user to play a game an return score interger, save as hi-score, if he play again and break 
previous hi-score update it'''
# import random

# def game():
#     print("You are playing a game")
#     score = random.randint(1,69)

#     # Fetch the hi-score
#     with open("hi-score.txt") as h:
#         hiscore= h.read()
#         if(hiscore!=""):
#             hiscore= int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your score: {score}")

#     if (score > hiscore): # write this hi-score to file
#         print("Its an high score")

#         with open("hi-score.txt", "w") as h:
#             h.write(str(score))

#     return score
# game()


''' Q3 get tables from 2 to 20 and place it in different files, and place this files in a folder'''

# def gentables(n):
#     table = ""
#     for i in range (1,11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open(f"table/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range (2,21):
#     gentables(i)

''' Q4 file contains Donkey, update it with ###### by updating it in same file'''

# word = "Donkey"

# with open("Donkey.txt", "r") as f:
#     content =f.read()

# contentNew = content.replace(word, "######")

# with open("Donkey.txt", "w") as f:
#     f.write(contentNew)

''' Q5 repeat 4th but for a list of such words to be censored'''

# words=["Donkey", "Monkey", "Shanty", "Bunty", "bad"]
# with open("Donkey.txt", 'r') as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "#" * len(word))

# with open("Donkey.txt", "w") as f:
#     f.write(content)


''' Q6 find out whether a file is identical & matches the content of other file'''
# with open("Donkey.txt") as f:
#     content1 = f.read()
# with open("domkey.txt") as f:
#     content2 = f.read()
# if(content1==content2):
#     print("Both files are identical")
# else:
#     print("are not same")

''' Q7 wipe out all the content the file'''

# with open("domkey.txt", 'w') as f:
#     f.write("")

''' Q8 rename a file ''' #take all content from old.txt and shift it to new.txt and delete old.txt,
                            # to delete file in python we need to use OS module or use shutil module
with open("old.txt") as f:
    content= f.read()

with open("new.txt", 'w') as f:
    f.write(content)