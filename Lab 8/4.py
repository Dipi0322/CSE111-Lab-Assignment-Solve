class Student:
    total = 0
    brac = 0
    other = 0

    def __init__(self,name,dep,school="BRAC University"):
        self.name = name
        self.dep = dep
        self.school = school
        Student.total += 1
        if school == "BRAC University":
            Student.brac += 1
        else:
            Student.other += 1

    def individualDetail(self):
        print(f"Name: {self.name}\nDepartment: {self.dep}\nInstitution: {self.school}")

    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {cls.total}\nBRAC University Student(s): {cls.brac}\nOther Institution Student(s): {cls.other}")

    @classmethod
    def createStudent(cls,name,dep,school="BRAC University"):
        obj = cls(name,dep,school)
        return obj
    
Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
