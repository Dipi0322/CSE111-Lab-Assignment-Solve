class NikeBangladesh:
  b = []
  stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
  sold = 0

  def __init__(self,loc):
    self.loc = loc
    self.d1 = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    self.s = 0
    NikeBangladesh.b.append(loc)

  def restockProducts(self,d):
    for i in d:
      if i in NikeBangladesh.stock:
        NikeBangladesh.stock[i] += d[i]
      if i in self.d1:
        self.d1[i] += d[i]


  def productSold(self,dic):
    for i in dic:
      if i in NikeBangladesh.stock:
        NikeBangladesh.stock[i] -= dic[i]
        NikeBangladesh.sold += dic[i]

      if i in self.d1:
        self.d1[i] -= dic[i]
        self.s += dic[i]

  def details(self):
    print(f"Nike {self.loc} Status:\nCurrently Stocked\n{self.d1}\nSold: {self.s}")

  @classmethod
  def status(cls):
    print(f"Nike Bangladesh Status:\nBranches Opened: {cls.b}\nCurrently Stocked\n{cls.stock}\nSold: {cls.sold}")

print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()