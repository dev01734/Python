"""Snake Water Gun Game"""
'''
1 for snake
-1 for water
0 for gun
'''

import random                                    # Library to generate a random nos
random_num = random.choice([-1, 0 ,1])
youstr=input("Choose one from S/G/W: ")
youD={"S":1, "W":-1, "G":0}
reverseDi={1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youD[youstr]

print( f"You Choose {reverseDi[you]}\nComputer Choose {reverseDi[random_num]}")


if(random_num == you):
    print("Draw")

# else:
#     if(random_num == -1 and you == 1):                random_num - you = -1-1 = -2
#         print("You Win")      
#     elif(random_num == -1 and you == 0):              -1
#         print("You Lose")
#     elif(random_num == 1 and you == -1):              2
#         print("You Lose")         
#     elif(random_num == 1 and you == 0):               1
#         print("You Win")
#     elif(random_num == 0 and you == -1):              1
#         print("You Win")
#     elif(random_num == 0 and you == 1):               -1
#         print("You Lose")



"""OR"""
'''accoding to the formula and patter we found (random_num - you) when its -1/2 you lose if 
            its -2/1 you win'''

if((random_num-you) == -1 or (random_num-you) == 2):
    print("you Lose")
elif((random_num-you) == -2 or (random_num-you) == 1):
    print("you win")
