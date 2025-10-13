import os

def words(word,color):
  if color=="red":
    print("\033[31m", word, "\033[0m", sep="", end="")
  elif color=="blue":
    print("\033[0;34m", word, "\033[0m", sep="", end="")
  elif color=="green":
    print("\033[0;32m", word, "\033[0m", sep="", end="")
  elif color=="white":
    print("\033[1;37m", word, "\033[0m", sep="", end="")
  elif color=="purple":
    print("\033[0;35m", word, "\033[0m", sep="", end="")
  else:
    print(word,end="")
    
print("MokeBeast")
mokebeast = {"Name": None, "Type": None, "Special Move": None, "Hp": None, "Mp": None}
for key in mokebeast.keys():
  mokebeast[key] = input(f"{key}: ")

print()
os.system("clear")
for name, value in mokebeast.items():
  if name == "Type":
    if value.upper() == "EARTH":
      words(f"{name}: {value}", "green")
    if value.upper() == "FIRE":
      words(f"{name}: {value}", "red")
    if value.upper() == "AIR":
      words(f"{name}: {value}", "white")
    if value.upper() == "WATER":
      words(f"{name}: {value}", "blue")
    if value.upper() == "SPIRIT":
      words(f"{name}: {value}", "purple")
    else:
      print(f"{name}: {value}")