

def myFunPositional(arg1, *argv):
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 

def myFunKeyworded(arg1, **kwargs):
    print ("First argument :", arg1)
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value))

print('\n')
myFunPositional('hello', 2, 3, 4)
print('\n')
myFunKeyworded('world', x=5, y=6, z=7)

def myFunc(x, y):
    print(x,y)

myFunc(y=5, x=6)