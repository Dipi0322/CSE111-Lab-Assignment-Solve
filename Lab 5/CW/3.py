class TaxiLagbe:
  def __init__(self,num,area):
    self.num = num
    self.area = area
    self.passenger = ""
    self.l = []
    self.count = 0
    self.fare = 0

  def addPassenger(self,*n):
    for i in n:
      if self.count < 4:
        self.count += 1
        passenger,fare = i.split("_")
        print(f"Dear {passenger}! Welcome to TaxiLagbe.")
        self.fare += int(fare)
        self.l.append(passenger)

      else:
        print("Taxi Full! No more passengers can be added.")

  def printDetails(self):
    x = ", ".join(self.l)
    print(f"Trip info for Taxi number: {self.num}\nThis taxi can only cover the {self.area} area.\nTotal passengers: {self.count}\nPassenger lists: \n{x}\nTotal collected fare: {self.fare} Taka")

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200','Matt_100')
taxi1.addPassenger('Wilson_105',"Dipi_100")
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()