'''
Created on 21/03/2014

@author: Beto
functions
'''
globalTen = 10

def changeGlobalTen():
    global globalTen # with global word the scope is out of this function
    globalTen = 15
    
    globals()['globalTen'] = 20 #another way to change it


def addNumbers(numOne=1, numTwo=1):
    return numOne+numTwo

def addxNumbers(*args):
    finalValue = 0 #local variable not in scope out of this function
    
    globalTen = 15 #this value not changed out of this function
    if args:
        for i in args:
           finalValue += i 
           #finalValue += i
        return finalValue
    else:
        return "please provice numbers"
    
def createDict(**kvargs):
    for i in kvargs:
        print i, kvargs[i]
    print type(kvargs)    
    return    
    
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)   

def main():
#    pass
    print addNumbers()
    print addNumbers(50,60)
    print addNumbers('Beto','Vickus')
    print addNumbers(34)
    #print addxNumbers('Beto','Vickus')
    print addxNumbers(12,23,12)
    print globalTen
    changeGlobalTen()
    print globalTen

    createDict(name='Derek',age=35,YearBorn=1974)
    createDict(Cust1=('Derek',35,1974),Cust2=('Paul',15,1994),Cust3=('Sally',25,1984))
    print factorial(100)

if __name__ == '__main__': main()  #define wich function will be called