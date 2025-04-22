"""Global : It changes the global variable even if the global is given"""
# if a =89 and 'global a' is not give it will print 89, but after global a is
#given it will change the value of global variable to the one given in 
# function and prints 3

a=89        #global variable
def fun():
    global a        #try me ctrl+/
    a=4     #local variable
    print(a)

fun()
print(a)