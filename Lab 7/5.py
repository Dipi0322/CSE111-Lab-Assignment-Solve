class BracuStudent:
  def __init__(self,n,home,p=False):
    self.n=n
    self.home=home
    self.p=p

  def get_pass(self):
    self.p = True

  def show_details(self):
    print(f"Student Name: {self.n}\nLives in {self.home}\nHave Bus Pass? {self.p}")

class BracuBus:
  def __init__(self,loc,cap=2):
    self.loc = loc
    self.cap = cap
    self.newL=[]
    self.count = 0

  def board(self,*obj):
    if len(obj) == 0:
      print(f"No passengers!")
    else:
      for i in range(len(obj)):
        if obj[i].home != self.loc:
          print("You got on the wrong bus!")
        elif obj[i].p == False:
          print("You don't have a bus pass!")
        else:
          if self.count < self.cap:
            print(f"{obj[i].n} boarded the bus")
            self.newL.append(obj[i].n)
            self.count += 1
          else:
            print("Bus is full!")

  def show_details(self):
    print(f"Bus Route: {self.loc}\nPassengers Count: {len(self.newL)} (Max: {self.cap})\nPassengers On Board: {self.newL}")

st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()