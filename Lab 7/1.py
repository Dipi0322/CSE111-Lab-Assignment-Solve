import math

class Circle:
  def __init__(self,rad):
    self.__rad = rad

  def getRadius(self):
    return self.__rad

  def setRadius(self,r):
    self.__rad = r

  def area(self):
    return math.pi * (self.__rad)**2

c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" , c1.area())


c2 = Circle(5)
print("Second circle radius:" , c2.getRadius())
print("Second circle area:" , c2.area())