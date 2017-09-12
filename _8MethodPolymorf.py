'''
Created on 25/03/2014

@author: Beto
iterate infinite number of attributes
inheritance
overide methods
polimorphism
how to ineritance of two or more classes
others..
'''
__metaclass__ = type  #enable new python 3.xx class  in python 2.7

class Animal:

   __name = "No Name"
   __owner = "No Owner"
   
   def __init__(self,**kvargs):
       self._attributes = kvargs
       
   def set_attributes(self, key, value):
       self._attributes[key] = value
       return
   
   def get_attributes(self,key):
       return self._attributes.get(key, None)
   
   def noise(self):
       print('errr')
       return
   
   def move(self):
       print("The animal moves forward")
       return
   
   def eat(self):
       print("Crunch Crunch")
       return
   
class Dog(Animal):
    
    def __init__(self, **kvargs):
        super(Dog, self).__init__()
        self._attributes = kvargs
        
    def noise(self):
        print("Woof Woof")
        Animal.noise(self)
        return
    
class Cat(Animal):
    
    def __init__(self, **kvargs):
        super(Cat, self).__init__()
        self._attributes = kvargs
        
    def noise(self):
        print("Meau")
        return
    
    def noise2(self):
        print("Purrrr")
        return
       
class Dat(Cat,Dog):
    
    def __init__(self, **kvargs):
        super(Dat, self).__init__()
        self._attributes =  kvargs
        
    def move(self):
        print("Chases tail")
        return            
       
def playWithAnimal(Animal):
    Animal.noise()
    Animal.eat()
    Animal.move()
    print(Animal.get_attributes('__name'))
    print(Animal.get_attributes('__owner'))
    print('\n')
    Animal.set_attributes('clean', 'Yes')
    print(Animal.get_attributes('clean'))
    
   
def main():
    jake = Dog(__name = 'Jake', __owner = 'Paul')
    sophie = Cat(__name = 'Sophie',__owner = 'Sue')
    Extrange = Dat(__name = 'alf', __owner = 'Beto')
    print 'gato :', 
    playWithAnimal(sophie)
    print ' perro :',
    playWithAnimal(jake)
    print ' DAT :',
    playWithAnimal(Extrange)
    Extrange.move()
    Extrange.noise()
    Extrange.noise2()
    print Extrange.get_attributes('__name')
    
    print "Cat is subclass of Animal" if (issubclass(sophie.__class__, Animal)) else "Cat is not subclass of Animal"
    #how to get the class of a variable?
    print Cat.__bases__
    print sophie.__class__
    print jake.__class__
    print sophie.__dict__
    
    vInt = 10
    print vInt.__class__
    print "vInt is subclass of Animal" if (issubclass(vInt.__class__, Animal)) else "vInt is not subclass of Animal"
    
if __name__ == '__main__': main()