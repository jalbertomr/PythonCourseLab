'''
Created on 21/03/2014

@author: Beto
'''
listEx = [4,5,6]
stringEx = "Random String"

print 3 in listEx   # False

print "String" in stringEx   # True

x = 1

# <> <= >= == !=
while x <= 30:
    print x
    x += 1
    
x = 0    
while x <= 30:
    print x,
    x += 1

listCustNum = [0,1,2]
listCustName = ['Bob smith', 'Helen Jones', 'Mark Summers']
listCustAge = [23,70,45]

print
for i in listCustNum:
    print '%d:%s is %d' % (listCustNum[i-1],listCustName[i-1],listCustAge[i-1])
    
listEx = [1,2,3,4]

for i in listEx:
    print i, listEx[i-1]
    
for i in range(1,32):
    print i
    
listEx = range(1,31)

for i in listEx:
    print i,
print

#lista generade en for con condicion en una linea sin :
print [i for i in listEx if i > 10]

    
for i in listEx:
    if (i%2) == 0:
        continue
    elif (i == 25):
        break
    else:
        print i,

print
#lista generade en for con condicion en una linea sin :
print [ i for i in listEx if i < 25 ]
print [ i for i in listEx if i%2 != 0]
print [ i for i in listEx if i < 25 and i%2 != 0]
print [ i for i in listEx if (i < 25) & (i%2 != 0)]

#lista generade en for con condicion en una linea sin :
print [i for i in listEx if ((i%2) != 0) ]

#Operating on Sequence Types
#for item in s          Iterate over items in s
#for tiem in sorted(s)  Iterate over the items of s in order
#for item in set(s)     Iterate over unique elements of s
#for item in reversed(s) Iterate over elements of s in reverse
#for itme in set(s).difference(t) Iterate over elements of s not in t
#for item in random.shuffle(s)  Iterate over elements of s in random order
