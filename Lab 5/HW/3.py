class Department:
    def __init__(self,dept="ChE",sec=5):
        self.dept = dept
        self.sec = sec
        self.total = 0
        self.merge_avg = 0
        print(f"The {self.dept} Department has {self.sec} sections.")

    def add_students(self,*students):
        self.avg = 0
        self.sum = 0
        self.sections = len(students)
        if len(students) == self.sec:
            for i in students:
                self.sum+=i
                self.avg = self.sum/self.sections
            print(f"The {self.dept} Department has an average of {self.avg} students in each section.")

        else:
            print(f"The {self.dept} Department doesn't have {len(students)}sections.")

    def merge_Department(self,*dep):
        self.total = self.avg * self.sec
        for i in dep:
            print(f"{i.dept} Department is merged to Engineering Department.")
            self.total += i.avg * i.sec
        self.merge_avg = self.total / self.sections
        return f"Now the {self.dept} Department has an average of {self.merge_avg} students in each section."

d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department') 
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))