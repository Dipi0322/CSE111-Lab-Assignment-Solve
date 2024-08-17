class Student:
  def __init__(self,name,id,dept="CSE"):
    self.name = name
    self.id = id
    self.dept = dept

  def dailyEffort(self,hr):
    self.hr = hr

  def printDetails(self):
    print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.dept}")
    x = "Suggestion: "
    if self.hr <= 2:
      x += "Should give more effort!"
    elif 2 < self.hr <= 4:
      x += "Keep up the good work!"
    else:
      x += "Excellent! Now motivate others."
    print(x)

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()