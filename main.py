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
    elif sides < 1:
      print("Number of sides is not valid. Enter a higher number.")
    else:
      "Invalid input. Try again."
userSides = int(input("How many sides? "))
rollDice(userSides)