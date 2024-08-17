# 3

class Contacts:
  def __init__(self,names,numbers):
    self.names = names
    self.numbers = numbers
    self.contactDict = self.contactDict()

  def contactDict(self):
    dic = {}
    if len(self.numbers) != len(self.names):
      print("Contacts cannot be saved. Length Mismatch!")
    else:
      print("Contacts saved succesffully")
      for i in range(len(self.names)):
        for j in range(len(self.numbers)):
          if i == j:
            dic[self.names[i]] = self.numbers[j]
    return dic


names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]

m1 = Contacts(names, numbers)
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")

names.append("Mother")
numbers.pop()

m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)