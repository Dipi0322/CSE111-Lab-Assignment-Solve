class Triangle:
  def __init__(self,b,h):
    self.__b=b
    self.__h=h

  def getBase(self):
    return self.__b

  def setBase(self,base):
    self.__b=base

  def getHeight(self):
    return self.__h

  def setHeight(self,height):
    self.__h = height

  def area(self):
    return 1/2 * self.__b * self.__h

t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())


t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())