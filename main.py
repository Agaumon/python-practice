import os
import random
import time

print("Character Creator")

def rollDice(sides):
  while True:
    if sides > 1:
      return random.randint(1, sides)
    else:
      print("Not enough sides on this dice")

def healthRoll():
    health = rollDice(6) * rollDice(12)
    health /= 2
    health += 10
    print("Health:",health)
    return health

def strengthRoll():
    strength = rollDice(6) * rollDice(12)
    strength /= 2
    strength += 12
    print("Strength:",strength)
    return strength

def menu(Player):
  print(Player,"Create your character")
  name = input("Name your character: ")
  time.sleep(1)
  os.system("clear")
  while True:
    type = input("Please choose a race: Human, Elf, Orc, Dwarf: ")
    if type.upper() == "HUMAN":
      type = "Human"
    elif type.upper() == "ELF":
      type = "Elf"
    elif type.upper() == "ORC":
      type = "Orc"
    elif type.upper() == "DWARF":
      type = "Dwarf"
    else:
      print("Please enter one of the listed races.")
      time.sleep(1)
      os.system("clear")
      continue
    while True:
      time.sleep(1)
      os.system("clear")
      print(name,"the",type)
      health = healthRoll()
      strength = strengthRoll()
      break
    break
player1 = menu(1)