class SultansDine:
  total = 0
  sell = 0
  d = []

  def __init__(self,loc):
    self.loc = loc
    self.s = 0
    SultansDine.total += 1
    SultansDine.d.append(loc)

  def sellQuantity(self,n):
    if n < 10:
      x = n * 300
    elif 10 <= n < 20:
      x = n * 350
    else:
      x = n * 400

    SultansDine.sell += x
    self.s += x
    SultansDine.d.append(self.s)

  def branchInformation(self):
    print(f"Branch Name: {self.loc}\nBranch Sell: {self.s} Taka")

  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {cls.total}\nTotal Sell: {cls.sell} Taka")
    for i in range(0,len(cls.d),2):
      print(f"Branch Name: {cls.d[i]}, Branch Sell: {cls.d[i+1]} Taka\nBranch consists of total sell's: {round((cls.d[i+1])/(cls.sell)*100,2)}%")


SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()