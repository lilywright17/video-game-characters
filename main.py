class character:
  name = None
  health = None
  magicPoints = None

  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints

  def print(self): 
    print()
    print("Character")
    print(f"Name: {self.name} \nHealth: {self.health} \nMagic Points: {self.magicPoints}")

class player(character):
  lives = None
  alive = None
  
  def __init__(self, name, health, magicPoints, lives, alive):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.lives = lives
    self.alive = alive

  def print(self): 
    print()
    print("Player")
    print(f"Name: {self.name} \nHealth: {self.health} \nMagic Points: {self.magicPoints} \nLives: {self.lives} \nAlive?: {self.alive}")

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, health, magicPoints, type, strength):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength

  def print(self): 
    print()
    print("Enemy")
    print(f"Name: {self.name} \nHealth: {self.health} \nMagic Points: {self.magicPoints} \nType: {self.type} \nStrength: {self.strength}")

class orc(enemy):
  speed = None

  def __init__(self, name, health, magicPoints, type, strength, speed):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.speed = speed

  def print(self): 
    print()
    print("Enemy")
    print(f"Name: {self.name} \nHealth: {self.health} \nMagic Points:   {self.magicPoints} \nType: {self.type} \nStrength: {self.strength} \nSpeed: {self.speed}")

class vampire(enemy):
  dayOrNight = None

  def __init__(self, name, health, magicPoints, type, strength, dayOrNight):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength
    self.dayOrNight = dayOrNight

  def print(self): 
    print()
    print("Enemy")
    print(f"Name: {self.name} \nHealth: {self.health} \nMagic Points: {self.magicPoints} \nType: {self.type} \nStrength: {self.strength} \nDay or night?: {self.dayOrNight}")

player1 = player("Lily", "50", "100", "9", "Yes")
player1.print()
vampire1 = vampire("Dracula", "2", "50", "Evil", "1000", "Night")
vampire1.print()
vampire2 = vampire("Mona", "5", "600", "Naughty", "899", "Day")
vampire2.print()
orc1 = orc("Shrek", "80", "800", "Mean", "5000", "700")
orc1.print()
orc2 = orc("Teddy", "65", "1000", "Nasty", "1001", "900")
orc2.print()
orc3 = orc("Dotty", "55", "900", "Mean", "7000", "1002")
orc3.print()

