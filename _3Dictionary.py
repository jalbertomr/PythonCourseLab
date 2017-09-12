'''
Created on 21/03/2014

@author: Beto
What is a Dictionary?
Like a List or Tuple, but with Key's instead of indexes
Age    Heigth    Weight
35    "6'3"      165
'''
import math

dictEx = {"Age":35,"Heigth":"6'3","Weight":165}

print dictEx.get("Heigth")
print "items", dictEx.items()
print "values", dictEx.values()
print "keys", dictEx.keys()

dictEx.pop("Heigth")
print "despues del pop", dictEx
dictEx.update({3:4})
dictEx["Heigth"] = "6'3"
print 'despues del "virtual push"' , dictEx

strName = 'Bob'
floatAge = 35.4456
charSex = 'M'
intKids = 2
boolMarried = True

print "My name is "+ strName
print "%s is %f years old" % (strName, floatAge)
print "%s is %.f years old" % (strName, floatAge)
print "%s is %.2f years old" % (strName, floatAge)
print 'Sex: %c' % (charSex)
print 'He has %d kids and said it\'s %s he is married' % (intKids,boolMarried)

print '%.15f' % (math.pi)
print '%20.15f' % (math.pi)
print '%-20.15f is the value of Pi' % (math.pi)

#precisionPi =  int(raw_input("How precise should pi be: "))
#print 'Pi = %.*f' % (precisionPi, math.pi)

bigString = 'Here is a long string .that I will be messing with'

print bigString[1:20:2]

print bigString.find('string')
print bigString.count('e')
print bigString.count('e',4)
print bigString.count('e',4 ,20)

copyStr =  tuple(bigString)
print copyStr
copyStr2 = ''.join(copyStr)
print copyStr2
print ','.join(copyStr)
print bigString.lower()
print bigString.upper()
print bigString.replace('long', 'replaced')
print bigString.split(' ')
print bigString.split('.')

randomWhite = '           Random white space    '
print randomWhite.strip()