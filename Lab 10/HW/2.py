class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(SportsPerson):
  def __init__(self, team_name, name, role, goal, play):
    super().__init__(team_name, name, role)
    self.goal = goal
    self.play = play

  def calculate_ratio(self):
    self.ratio = self.goal / self.play

  def print_details(self):
    print(super().get_name_team())
    print(f"Team Role: {self.role}\nTotal Goal: {self.goal}, Total Played: {self.play}\nGoal Ratio: {self.ratio}\nMatch Earning: {(self.goal*1000)+(self.play*10)}K")

class Manager(SportsPerson):
  def __init__(self, team_name, name, role, win):
    super().__init__(team_name, name, role)
    self.win = win
    
  def print_details(self):
    print(super().get_name_team())
    print(f"Team Role: {self.role}\nTotal Win: {self.win}\nMatch Earning: {self.win*1000}K")

player_one = Player('Al-Nassr', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()

