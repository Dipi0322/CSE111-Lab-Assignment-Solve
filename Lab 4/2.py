class Panda:
  def __init__(self,name,gender,age):
    self.name = name
    self.gender = gender
    self.age = age

  def sleep(self,hr):
    x = f"{self.name} sleeps {hr} hours daily and should have "
    if 3 <= hr <= 5:
      x += "Mixed Veggies"
    elif 6 <= hr <= 8:
      x += "Eggplant & Tofu"
    elif 9 <= hr <= 11:
      x += "Broccoli Chicken"
    else:
      x += "bamboo leaves"

    return x

panda1 = Panda("Kunfu", "Male", 5)
panda2 = Panda("Pan Pan", "Female",3)
panda3 = Panda("Ming Ming", "Female",8)

print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))

print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))

print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep(13))