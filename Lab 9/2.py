class Player:
  total = 0
  l = []

  def __init__(self,name=None,num=10,team=None):
    self.name = name
    self.num = num
    self.team = team
    Player.total += 1

    Player.l.append(self)

  def set_name(self,n):
    self.name = n
    # Player.l.append(self)

  def set_team(self,t):
    self.team = t

  def set_number(self,nu):
    self.num = nu

  def player_detail(self):
    return f"Player Name: {self.name}\nJersey Number: {self.num}\nCountry: {self.team}"


  @classmethod
  def info(cls):
    print(f"Total number of players: {cls.total}")
    new = ""
    for i in cls.l:
      if new == "":
        new += i.name
      else:
        new += ", " + i.name
    print(f"Players enlisted so far: {new}")

print("Total number of players:", Player.total)
print("---------------------------")
p1 = Player()
p1.set_name("Neymar")
p1.set_team("Brazil")
print(p1.player_detail())
print('========================')
Player.info()
print("---------------------------")
p2 = Player("Ronaldo")
p2.set_number(7)
p2.set_team("Portugal")
print(p2.player_detail())
print('========================')
Player.info()
print("---------------------------")
p3 = Player("Messi")
p3.set_team("Argentina")
print(p3.player_detail())
print('========================')
Player.info()
print("---------------------------")
p4 = Player("Mbappe", 10, "France")
print(p4.player_detail())
print('========================')
Player.info()
