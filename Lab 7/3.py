class Team:
  def __init__(self,n=None):
    self.__n = n
    self.__l = []

  def getName(self):
    return self.__n

  def setName(self,s):
    self.__n = s

  def addPlayer(self,p_obj):
    self.__l.append(p_obj.name)

  def printDetail(self):
    print(f"=====================\nTeam:{self.__n}\nList of Players:\n{self.__l}\n=====================")


class Player:
  def __init__(self,name):
    self.name = name

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
