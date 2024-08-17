class GreenPhone:
  def __init__(self,model,android_ver,cameras):
    self.model = model
    self.android_ver = android_ver
    self.cameras = cameras
    self.update_count = 0

  def showSpecification(self):
    print(f"Phone Company: GreenPhone\nModel Name: {self.model}\nAndroid Version: {self.android_ver}\nNumber of Cameras: {self.cameras}")

  def updatePhone(self):
    if self.model[0] == "A":
      if self.update_count < 2:
        self.update_count += 1
        self.android_ver += 1
        print(f"Your phone Greenphone {self.model} is upgraded to Android Version: {self.android_ver}")
      else:
        print(f"Your phone Greenphone {self.model} is already up to date.")

    elif self.model[0] == "M":
      if self.update_count < 3:
        self.update_count += 1
        self.android_ver += 1
        print(f"Your phone Greenphone {self.model} is upgraded to Android Version: {self.android_ver}")
      else:
        print(f"Your phone Greenphone {self.model} is already up to date.")

    elif self.model[0] == "U":
      if self.update_count < 4:
        self.update_count += 1
        self.android_ver += 1
        print(f"Your phone Greenphone {self.model} is upgraded to Android Version: {self.android_ver}")
      else:
        print(f"Your phone Greenphone {self.model} is already up to date.")

print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()