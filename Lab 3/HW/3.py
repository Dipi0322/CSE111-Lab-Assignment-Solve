class box:
    def __init__(self,list):
        self.list = list
        self.unpack = self.unpack()
        print("Creating a box!")

    def unpack(self):
        l = self.list
        for i in range(len(l)):
            if i == 0:
                self.height = l[0]
            elif i == 1:
                self.width = l[1]
            elif i == 2:
                self.breadth = l[2]


print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
volume = b1.height * b1.width * b1.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
volume = b3.height * b3.width * b3.breadth
print(f"Volume of the box is {volume} cubic units.")
print(b2.width)

# one = (b3 == b2)
# print(one)

# b3.width = 100
# two = (b3 == b2)
# print(two)
# print(b2.width)