class Passenger:
    count = 0

    def __init__(self,name):
        Passenger.count += 1
        self.name = name
        self.fare = 450

    def set_bag_weight(self,weight):
        if 21 <= weight <= 50:
            self.fare += 50
        elif weight > 50:
            self.fare += 100

    def printDetail(self):
        print(f"Name: {self.name}\nBus Fare: {self.fare} taka")

print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)

