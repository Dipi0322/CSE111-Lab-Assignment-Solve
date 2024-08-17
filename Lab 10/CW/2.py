class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self):
        self.y += 1
    def moveDown(self):
        self.y -= 1
    def moveRight(self):
        self.x += 1
    def moveLeft(self):
        self.x -= 1
    def detail(self):
        return '('+str(self.x)+' , '+str(self.y)+')'

class Vehicle2010(Vehicle):
    def __init__(self):
        super().__init__()
    def moveUpperRight(self):
        super().moveRight()
        super().moveUp()
    def moveUpperLeft(self):
        super().moveLeft()
        super().moveUp()
    def moveLowerRight(self):
        super().moveRight()
        super().moveDown()
    def moveLowerLeft(self):
        super().moveDown()
        super().moveLeft()
    def equals(self,obj):
        if obj.x == self.x and obj.y == self.y:
            return True
        else:
            return False

print('Part 1')
print('------')
car = Vehicle()
print(car.detail())
car.moveUp()
print(car.detail())
car.moveLeft()
print(car.detail())
car.moveDown()
print(car.detail())
car.moveRight()
print(car.detail())
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1.detail())
car1.moveLowerLeft()
print(car1.detail())
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))