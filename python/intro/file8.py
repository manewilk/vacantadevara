# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

import sys

if len(sys.argv) < 4:
    print ('Usage <value1> <value2> <value3>')
    sys.exit ( 1 )
    
nr1 = sys.argv[1]
nr2 = sys.argv[2]
nr3 = sys.argv[3]

def myfunc(nr1,nr2,nr3):
    if nr1 > nr2 and nr1 > nr3:
        print("Numarul cel mai mare este: ", nr1)
    elif nr2 > nr1 and nr2 > nr3:
        print("Numarul cel mai mare este: ", nr2)
    else:
        print("Numarul cel mai mare este: ", nr3)

myfunc(nr1,nr2,nr3)
