print("Rainbo-izer for Sentences")

def colorChange(color):
  if color == "r":
    print("\033[0;31m", end="")
  if color == " ":
    print("\033[0m", end="")
  if color == "b":
    print("\033[0;34m", end="")
  if color == "g":
    print("\033[0;32m", end="")
  if color == "p":
    print("\033[0;35m", end="")
  if color == "y":
    print("\033[1;33m", end="")

sentence = input("Write out a sentence: ")

for letters in sentence:
  colorChange(letters.lower())
  print(letters, end="")