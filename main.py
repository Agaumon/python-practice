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

def menu():
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
  return name, type, health, strength

print("Player 1:")
player1_name, player1_type, player1_health, player1_strength = menu()

print("Player 2:")
player2_name, player2_type, player2_health, player2_strength = menu()

print()
print("Player 1:",player1_name,"the",player1_type)
print("Health:",player1_health,"Strength:",player1_strength)
print()
print("Player 2:",player2_name,"the",player2_type)
print("Health:",player2_health,"Strength:",player2_strength)