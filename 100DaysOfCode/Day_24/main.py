import random

print("Infinity Dice")
def rollDice(sides):
  while True:
    if sides > 1:
      print(random.randint(1,sides))
      replay = input("Roll again? ").upper()
      if replay == "YES" or replay == "Y":
        continue
      elif replay == "NO" or replay == "N":
        print("Aww okay bye")
        break
    else:
      print("Invalid input. Try again.")
      break
userSides = int(input("How many sides? "))
rollDice(userSides)