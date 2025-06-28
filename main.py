import random

print("Character Stats Generator")

def baseStat(sides):
  return random.randint(1,sides)

def rollDice():
  roll6 = baseStat(6)
  roll8 = baseStat(8)
  newStat = roll6 * roll8
  return newStat

name = input("Enter character name: ")
while True:
  if name:
    print("Their health is", newStat)