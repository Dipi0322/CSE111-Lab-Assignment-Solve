import math

class Sphere:
  def __init__(self,id,r=1,clr="White"):
    self.id = id
    self.r = r
    self.clr = clr
    self.v = self.calc_v()

  def calc_v(self):
    return (4/3) * math.pi * (self.r) ** 3

  def printDetails(self):
    print(f"Sphere ID: {self.id}\nColor: {self.clr}\nVolume: {self.v}")

  def merge_sphere(self,*sphere):
    print("Spheres are being merged")
    for i in sphere:
      self.v += i.v
      if self.clr != i.clr:
        self.clr = "Mixed Color"

sphere1 = Sphere("Sphere 1")
print("1***************")
sphere1.printDetails()
print("2***************")
sphere2 = Sphere("Sphere 2", 3)
print("3***************")
sphere2.printDetails()
print("4***************")
sphere3 = Sphere("Sphere 3", 2)
print("5***************")
sphere3.printDetails()
print("6***************")
sphere3.merge_sphere(sphere1,sphere2)
print("7***************")
sphere3.printDetails()
print("8***************")
sphere4 = Sphere("Sphere 4", 5, "Purple")
print("9***************")
sphere4.merge_sphere(sphere3)
print("10***************")
sphere4.printDetails()
