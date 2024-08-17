class Spaceship:
  def __init__(self,name,cap):
    self.name = name
    self.cap = cap
    self.newWeight = 0
    self.l = []

  def load_cargo(self,n_obj):
    if (self.newWeight + n_obj.getWeight()) < self.cap:
      self.l.append(n_obj.getName())
      self.newWeight += n_obj.getWeight()
    else:
      print(f"Warning: Unable to load {n_obj.getName()} insid {self.name}. Exceeds capacity by {(self.newWeight + n_obj.getWeight())-self.cap}")

  def display_details(self):
    print(f"Spaceship Name: {self.name}\nCapacity: {self.cap}\nCurrent Cargo Weight: {self.newWeight}\nCargo: {self.l}")

class Cargo:
  def __init__(self,n,w):
    self.__n=n
    self.__w=w

  def getName(self):
    return self.__n

  #def setName(self,n):
    #self.__n = n

  def getWeight(self):
    return self.__w

# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()