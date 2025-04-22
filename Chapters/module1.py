
"""if __name == "__main" is used to import a function from other file and run it 
but code inside if __name == "__main" will only run if its present in main file
not in the from where its imported"""

#Eg. module1.py & namemain1.py

def myfunc():
    print("Hiii")

if __name__=="__main__":
    #If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myfunc()
    print(__name__)
