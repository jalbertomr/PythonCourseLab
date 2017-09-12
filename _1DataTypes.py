'''
Created on 19/03/2014

@author: Beto
de los webinarios de Derek Banas
'''
# comments
import math
from math import sqrt

integerEx = 8
longintEx = 200000000L
floatEx = 2.434
stringEx = "Hello"
booleanEx = True

print type(integerEx)
print type(longintEx)
print type(floatEx)
print type(stringEx)
print type(booleanEx)

#how to iterate in DataTypes
#for tipo in DataTypes
#  print tipo

booleanTwo = False

print booleanEx and booleanTwo
print booleanEx or booleanTwo
print not booleanEx

intOne = 7
intTwo = 99
floatOne = 7.9
floatTwo = 9.9

print intTwo / intOne
print float(intTwo) / float(intOne)
print int(floatOne)

print int(booleanEx)
print int(not booleanEx)

print intOne + intTwo
print intOne - intTwo
print intOne * intTwo
print intOne / intTwo
print intOne ** intTwo
print intOne % intTwo

print math.log(intOne)
print sqrt(intOne)

answer = raw_input('Cual es tu nombre...')
print 'Hello ' + answer
print "Hello",answer

longStr = '''This is a very long long \
string that goes on and on and on'''

print longStr

print 'he said'
print "he said 'hi what are you doing'\n"
print 'he said \'hi what are you doing\''

print range(1,100)
