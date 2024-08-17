class StudentDatabase:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = {}

    def calculateGPA(self,l,sem):
        temp = {}
        courses = []
        cgpa = 0
        for i in l:
            course,cg = i.split(":")
            courses.append(course)
            cgpa += float(cg) * 3

        total = cgpa / (len(l)*3)
        total = round(total,2)
        t = tuple(courses)
        temp[t] = total
        self.grades[sem] = temp

    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.id}")
        for key,val in self.grades.items():
            print(f"Courses taken in {key}: ")
            for k,v in val.items():
                for i in k:
                    print(i)
                print(f"GPA: {v}")

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()
