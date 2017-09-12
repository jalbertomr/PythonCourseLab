'''
created on 26/03/2014

@author: Beto
File IO
'''

import os

def retriveFile():
    try:
        bestStudent = {}  # create empty dictionary
        bestStudentStr = "The Best Students Ranked\n\n"
        
        f = open('studentgrades.txt')   #,['r'|'w'|'a'])
        
    except(IOError), e:
        print "file not found"
        
    else:
        for line in f:
            name, grade = line.split()
            bestStudent[grade] = name
        f.close()
        
        for i in sorted(bestStudent.keys(), reverse=True):
            print "%10s scored a %s" % (bestStudent[i], i)
            print bestStudent[i] + ' scored a ' + i
            #bestStudentStr += bestStudent[i] + ' scored a ' + i + '\n'
            #bestStudentStr += "%10s scored a %s\n" % (bestStudent[i], i)
        print '\n'
        
        print bestStudentStr
        
        outToFile = open('studentrank.txt','w')
        outToFile.write(bestStudentStr)
        outToFile.close()
        
        print "Finished Output"
    return    
    
def main():
    retriveFile()

if __name__ == '__main__': main()