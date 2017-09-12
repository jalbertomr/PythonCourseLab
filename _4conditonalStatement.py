'''
Created on 21/03/2014

@author: Beto
'''


'''
yourAge = int(raw_input('How old are you: '))

if (yourAge > 0) and (yourAge < 120):
    if (yourAge == 35):
        print "Same as me"
    elif (yourAge > 35):
        print "Older than me"
    else:
        print "Younger than me"
else:
    print "Don't lie about your age"
print
'''
#Conditional Expression

x, y = 1, 0  #default values
g = 'varDefinida'
g = None
# del g      #desdefine g

try:
    x = int(raw_input("dame un numero: "))
except:
    # x se queda con el default   
    pass

# {valor = asignado si TRUE} if condicion else {valor asignado si FALSE}  
a = 'y is less than x' if ( y < x) else 'x is less or equal than y'
print x, y, a
print "valor de x:%d valor de y:%d por lo tanto %s " % (x,y,a) 

if ( y < x ): 
    a = 'condicion verdadera' 
else: 
    a='condicion false'
2print x, y, a
     