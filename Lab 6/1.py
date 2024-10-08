class Teacher:
  def __init__(self,name,dep):
    self.n=name
    self.d=dep
    self.lst1=[]

  def addCourse(self,c_obj):
    self.lst1.append(c_obj)

  def printDetail(self):
    print("========================")
    print(f"Name: {self.n}")
    print(f"Department: {self.d}")
    print("List of Courses")
    print("========================")
    for item in self.lst1:
      print(item.c)
    print("========================")

class Course:
  def __init__(self,course):
    self.c=course


t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()