class Farmer:
  def __init__(self,n=None):
    self.n = n
    self.crop = ""
    self.fish = ""
    self.c1 = 0
    self.c2 = 0

    if type(n) == str:
      print(f"Welcome to your farm, {self.n}")
    elif type(n) == int:
      print(f"Welcome to your farm. Your farm ID is {self.n}")
    else:
      print("Welcome to your farm!")

  def addCrops(self,*crop):
    self.len1 = len(crop)
    if len(crop) == 0:
      print("No crop(s) added.")
    else:
      print(f"{len(crop)} crop(s) added.")

    for i in crop:
      self.c1 += 1
      if len(self.crop) == 0:
        self.crop += i
      else:
        self.crop += ", " + i

  def addFishes(self,*fish):
    self.len2 = len(fish)
    if len(fish) == 0:
      print("No fish added.")
    else:
      print(f"{len(fish)} fish(s) added.")

    for i in fish:
      self.c2 += 1
      if len(self.fish) == 0:
        self.fish += i
      else:
        self.fish += ", " + i

  def showGoods(self):
    if self.len1 == 0:
      print("You don't have any crop(s).")
    else:
      print(f"You have {self.len1} crop(s):\n{self.crop}")

    if self.len2 == 0:
      print("You don't have any fish(s).")
    else:
      print(f"You have {self.len2} fish(s):\n{self.fish}")


f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")
