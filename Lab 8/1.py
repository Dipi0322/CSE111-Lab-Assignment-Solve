class Student:
    id = 0

    def __init__(self,name,dep,age,cg):
        Student.id += 1
        self.name = name
        self.dep = dep
        self.age = age
        self.cg = cg

    def showDetails(self):
        print(f"ID: {Student.id}\nName: {self.name}\nDepartment: {self.dep}\nAge: {self.age}\nCGPA: {self.cg}")

    @classmethod
    def from_String(cls,s):
        name,dep,age,cg = s.split("-")
        obj = cls(name,dep,age,cg)
        return obj
    
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails() 
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails() 
