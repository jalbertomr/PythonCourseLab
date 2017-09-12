'''
Created on 21/03/2014

@author: Beto
objecct, attributes, instance, methods
'''
class Animal:
    
    __hungry = "yes"     #private attributes
    __name = "No name"   #private attributes
    __owner = "No Owner" #private attributes

    def __init__(self):
        pass
    
    def set_owner(self, newOwner):
        self.__owner = newOwner
        return
    
    def get_owner(self):
        return self.__owner
    
    def set_name(self, newName):
        self.__name = newName
        return
    
    def get_name(self):
        return self.__name

    def noise(self):
        print("errr")
        self.__hiddenMethod()
        return
    
    def __hiddenMethod(self):
        print("hard to reach")
        return
    
def main():
    dog = Animal()
    
    dog.set_owner('Sue')
    print dog.get_owner()
    
    #print dog.__owner     #not reachable because private attribute
    #print dog.__hiddenMethod()  #not reachable because private method
    dog.noise()
    
if __name__ == '__main__': main()