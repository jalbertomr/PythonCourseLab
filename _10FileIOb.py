'''
Created on 27/03/2014

@author: Beto
'''
import os

def directoryPlay():
    print os.curdir
    print os.path
    print os.pathsep
    print os.listdir('.')
    for node in os.listdir('.'):
        print node
        
    print os.path.isdir('../tests')
    print os.path.isfile('test2') 
    
    dirList = os.listdir('/Mis documentos/')
    for node in dirList:
        if os.path.isdir('/Mis documentos/' + node):
            print 'Dir:' + node + ': ', 
            print os.listdir('/Mis documentos/' + node)  
        else:
            print 'file:' + node,
        
    if (os.path.exists('AcaToyBorrame') == False):
        os.mkdir('AcaToyBorrame')
        print 'Directorio Creado'
    else:
        print 'Directorio Ya existia'    
    
    return

def main():
    directoryPlay()

if __name__ == '__main__': main()