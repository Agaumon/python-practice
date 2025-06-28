import random

print("Character Stats Generator")

def baseStat(number):
  base = ""
  for i in range(number):
    random.randint(1,number)
    return base

def rollDice():
  while True:
    roll6 = random.randint(1,6)
    roll8 = random.randint(1,8)
    print(roll6)
    print(roll8)
    stats = roll6 * roll8
    return stats

baseStats = baseStat(6)
finalStats = rollDice()