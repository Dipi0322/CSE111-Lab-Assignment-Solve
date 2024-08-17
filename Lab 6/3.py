class Vaccine:
    def __init__(self,n,c,l):
        self.n = n
        self.c = c
        self.l = l

class Person:
    def __init__(self,n,a,j="General Citizen"):
        self.n = n
        self.a = a
        self.j = j
        self.count = 0
        self.dic = {}

    def pushVaccine(self,vac_obj,d="1st Dose"):
        if self.j != "Student" and self.a < 25:
            print(f"Sorry {self.n}, Minimum age for taking vaccines is 25 years now.")

        else:
            if self.count == 0:
                self.dic[self.n] = vac_obj.n
                print(f"1st dose done for {self.n}")
                self.vac = vac_obj.n
                self.return_again = vac_obj.l
                self.count += 1
            else:
                if vac_obj.n != self.dic[self.n]:
                    print(f"Sorry {self.n}, you can’t take 2 different vaccines")
                else:
                    print(f"2nd Dose done for {self.n}")
                    self.vac = vac_obj.n
                    self.count += 1

    def showDetail(self):
        print(f"Name: {self.n} Age: {self.a} Type: {self.j}\nVaccine name: {self.vac}")
        if self.count == 1:
            print(f"1st Dose: Given\n2nd Dose: Please come after {self.return_again} days")
        else:
            print(f"1st Dose: Given\n2nd Dose: Given")

astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")