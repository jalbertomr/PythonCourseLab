'''
Created on 26/03/2014

@author: Beto
Exception Handling
'''
import exceptions

class Dog:
    __secret = 2

def main():
    #---to print all de exceptions
    #for i in dir(exceptions):
    #    print i
    
    #--- to reach an Exception    
    #raise Exception('JustDisagreeable')
    
    # ---instance has no attribute exception
    #puppy = Dog()
    #print puppy.__secret
    
    # ---input ouputexception
    #f = open('inexistenfile.txt')
    
    #--- index error, key error
    #list = [1,2,3]
    #print list[3]
    #---dict = ({'Age':34})
    #print dict['Notkey']
    #---name error
    #print notvariable
    #---arguments error
    #print 'Tomato' % 5
    #---division error
    #zeroDivision = 1/0

    #--- how to handle
    try:
       ZeroDivision= 1/0
    except ZeroDivisionError:
       print "You can't divide by zero"    
    
    try:
        ZeroDivision = notHere/0
    except (NameError,ZeroDivisionError):
       print "You can't divide by zero"    
        
    try:
        ZeroDivision = notHere/0
    except (NameError,ZeroDivisionError), e:
       print "You can't divide by zero"    
       print e
       
    try:
        ZeroDivision = 1.0/2.0
    except (NameError,ZeroDivisionError):
       print "You can't divide by zero"    
    else:
        print ZeroDivision    
        
    try:
        ZeroDivision = 1.0/0
    except (NameError,ZeroDivisionError):
       print "You can't divide by zero"    
    else:
        print ZeroDivision    
    finally:
        print "Everything is ok"
              
if __name__ == '__main__': main()