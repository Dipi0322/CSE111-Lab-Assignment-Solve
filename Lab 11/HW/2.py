class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
        
    def examSyllabus(self):
        return "Maths , English"
    
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
    
class ScienceExam(Exam):
    def __init__(self, marks, time, *sub):
        super().__init__(marks)
        self.time = time
        self.sub = sub

    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.sub)+2}"
    
    def examSyllabus(self):
        x = super().examSyllabus() + ", " + ", ".join(self.sub)
        return x
    
    def examParts(self):
        x = super().examParts()
        for i in range(len(self.sub)):
            if i != 0:
                x += f"\nPart {i+3} - {self.sub[i]}"
            else:
                x += f"Part {i+3} - {self.sub[i]}"
        return x
    
    
engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================') 
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())

