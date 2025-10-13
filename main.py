import os

print("MokeBeasts")

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

mokebeast = {"Name": "", "Type": "", "Special Move": "", "HP": "", "MP": ""}

for key in mokebeast:
  mokebeast[key] = input(f"{key}: ")

print()
os.system("clear")

for name, value in mokebeast.items():
  print(f"{name}: {value}")