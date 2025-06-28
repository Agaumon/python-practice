import random

print("Character Stats Generator")

def baseStat(sides):
  return random.randint(1,sides)

def rollDice():
  roll6 = baseStat(6)
  roll8 = baseStat(8)
  newStat = roll6 * roll8
  return newStat

while True:
  name = input("Enter character name: ")
  if name:
    stats = rollDice()
    print("Their health is", stats, "hp")
    
    again = input("Generate another character? (yes/no): ").lower()
    if again != "yes" and again != "y":
      break
  else:
    print("Please enter a valid name!")

print("Thanks for playing!")