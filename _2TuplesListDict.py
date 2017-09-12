'''
Created on 19/03/2014

@author: Beto
tuples, List and Dictionaries are like arrays
Customer[0] = 'Bob'
Customer[-1] = True
Customer[5] = True
  0    1    2    3      4     5
'Bob'  38  'M'   1971   2.5   True
-6     -5   -4   -3    -2    -1

Dictionaries have Keys and Values
Name   Age    Sex   Birth
'Bob'  38    'M'    '12/21/1971'

'''

TuplesEx = ('Derek', 35, 'Pittsburg', 'PA', 'PA')
print TuplesEx
print TuplesEx[0:0], "TuplesEx[0:0]"
print TuplesEx[0:2], "TuplesEx[0:2]"
print TuplesEx[0:3], "TuplesEx[0:3]"
print TuplesEx[0:4], "TuplesEx[0:4]"
print TuplesEx[1:2], "TuplesEx[1:2]"
print TuplesEx[1:3], "TuplesEx[1:3]"
print TuplesEx[1:], "TuplesEx[1:]"
print "Se observa [elementos inician en 0:elementos inician en 1]"
print TuplesEx[1:-1], "TuplesEx[1:-1]"
print TuplesEx[1:-1:2], "TuplesEx[1:-1:2]" # del elemento 1 al penultimo de dos en dos
print TuplesEx[2:2], "TuplesEx[2:2]"
print TuplesEx[2]  , "TuplesEx[2]"
print "Aqui estoy:" ,TuplesEx.count('PA'), "TuplesEx.count('PA')"
print TuplesEx.index(35 )
tupleEx2 = tuple('abcd')
print tupleEx2

print tupleEx2[0]
print tupleEx2[0:2]

listEx = ['Derek', 35, 'Pittsburg', 'PA','PENultimo','ULTIMO']
print "Aqui estoy:"+ str(listEx.count('PA'))
print "Aqui estoy:", listEx.count('PA')
print listEx
print listEx[2], "listEx[2]"
print listEx[-2], "listEx[-2]"
print listEx[-2:], "listEx[-2:]"


listEx2 = tuple('abcd')
print listEx2, "tuple('abcd')"

listNum = [1,2,3,4,5,6,7,8,9,10]
for num in listNum:
    print num ,":", listNum[num-1],",",
print 

print listNum
print listNum[0:0], "listNum[0:0]"
print listNum[0:2], "listNum[0:2]"
print listNum[0:3], "listNum[0:3]"
print listNum[0:4], "listNum[0:4]"
print listNum[1:2], "listNum[1:2]"
print listNum[1:3], "listNum[1:3]"
print listNum[1:], "listNum[1:]"
print listNum[4:9], "listNum[4:9]"
print "Se observa [elementos inician en 0:elementos inician en 1]"
print listNum[1:-1], "listNum[1:-1]"
print listNum[1:-1:2], "listNum[1:-1:2]" # del elemento 1 al penultimo de dos en dos
print listNum[2:2], "listNum[2:2]"
    
print listNum[-3:]
print listNum[:3]
print listNum[1:10:2]

print len(listNum), "len(listNum)"
print max(listNum), "max(listNum)"

listName = list('Fred')
print listName, "list(fred)"

listName[4:] = 'dy' 
print "listName[4:] = 'dy'"
print "une elementos de la lista '[caracteres entre elementos]'.join(list)"
print ''.join(listName), "''.join(listName)"
print ', '.join(listName), "', '.join(listName)"
print '###'.join(listName), "'###'.join(listName)"
print "##".join("34234"), '"##".join("34234")'

listEx2 = [1,2,3,4]
listEx2[1] = 5
print listEx2

del listEx2[1]
print listEx2

listEx.append('Joy')
print listEx
listEx.remove('Joy')
print listEx
listEx.remove(listEx[3])
print listEx
listEx.insert(2, 'BetoInsertado')
print listEx

listEx2 = ['f','e','c','d','a','b']
listEx2.sort()
print listEx2

listEx3 = [['a','b','c'],
           ['d','e','f'],
           ['g','h','i']]
print listEx3
print listEx3[2][1]