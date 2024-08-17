# 2 (i)

class MangoTree:
  def __init__(self,variety,height=1,number_of_mangoes =0):
    self.variety = variety
    self.height = height
    self.number_of_mangoes = number_of_mangoes


mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

# (ii)
print("Updated details after 5 years:")
print("=====================================")
print(f"Variety: {mangoTree1.variety}")
mangoTree1.height = 16
print(f"Height: {mangoTree1.height} meter(s)")
if mangoTree1.variety == "Amrapali":
  mangoTree1.number_of_mangoes = mangoTree1.height * 15
  print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
else:
  mangoTree1.number_of_mangoes = mangoTree1.height * 10
  print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
# Display the details of the mango tree
print(f"Variety: {mangoTree2.variety}")
mangoTree2.height = 16
print(f"Height: {mangoTree2.height} meter(s)")
if mangoTree2.variety == "Amrapali":
  mangoTree2.number_of_mangoes = mangoTree2.height * 15
  print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
else:
  mangoTree2.number_of_mangoes = mangoTree2.height * 10
  print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")