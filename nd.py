class Animal:
   legs = '0'

   def __init__(self):
      pass

   def whoAmI(self):
      print ("Animal")
 
   def eat(self):
      print ("Eating")
   def wight(seft):
      print ("wight 88");
class Entity:
   def __init__(self):
      pass

 
class Dog(Entity, Animal):
   def __init__(self):
      Animal.__init__(self)
      Entity.__init__(self)
      print ("Dog created")
      self.legs = '4';
 
   def whoAmI(self):
      print ("Dog go go")
 
   def eat(self):
      print ("eat eat eat .....")

   def run(self):
      print ("legs: " + self.legs + " run run run .....")
 
 
d = Dog()
d.whoAmI()
d.eat()
d.run()
d.wight()