class Student:
    def __init__(self,name,id,cg):
        self.name = name
        self.id = id
        self.cg = cg

    def setId(self,n):
        self.id = n

class Department:
    def __init__(self,dep):
        self.dep = dep
        self.l = []
        self.id = {}

    def addStudent(self,*s_objs):
        for s_obj in s_objs:
            if s_obj.id in self.id:
                print("Student with the same ID already exists, Please try with another ID")
            else:
                self.l.append(s_obj)
                self.id[s_obj.id] = f"{s_obj.name}-{s_obj.cg}"
                print(f"Welcome to {self.dep} department, {s_obj.name}")

    def findStudent(self,id):
        if id not in self.id:
            print("Student with this ID doesn't exist, Please give a valid ID")
        else:
            n,c = self.id[id].split("-")
            print(f"Student info:\nStudent Name: {n}\nID: {id}\nCGPA: {c}")

    def details(self):
        print(f"Department: {self.dep}\nNumber of Student: {len(self.l)}")
        for k,v in self.id.items():
            n,c = v.split("-")
            print(f"Student Name: {n},ID: {k},CGPA: {c}")

s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()