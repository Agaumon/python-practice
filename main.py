import os
import random
import time

print("Character Creator")

def rollDice(sides):
  while True:
    if sides > 1:
      random.randint(1, sides)
    else:
      print("Not enough sides on this dice")

def healthRoll():
  while True:
    health = rollDice(6) * rollDice(12)
    health /= 2
    health += 10
    print("Health:",health)

def strengthRoll():
  while True:
    strength = rollDice(6) * rollDice(12)
    strength /= 2
    strength += 12
    print("Strength:",strength)

def menu():
  name = input("Name your character: ")
  type = input("Please choose a race: Human, Elf, Orc, Dwarf: ")
  while True:
    time.sleep(1)
    print(name,"the",type)
    healthRoll()
    strengthRoll()
    break

menu()