import os

print("MokeBeasts")

mokebeast = {"Name": "", "Type": "", "Special Move": "", "HP": "", "MP": ""}

for key in mokebeast:
  mokebeast[key] = input(f"{key}: ").capitalize

print()
os.system("clear")

type_value = ""
for name, value in mokebeast.items():
  if name == "Type":
    type_value = value.upper()
    if type_value == "EARTH":
      color = "\033[0;32m"  # green
    elif type_value == "FIRE":
      color = "\033[0;31m"  # red
    elif type_value == "AIR":
      color = "\033[0m"     # white/normal
    elif type_value == "WATER":
      color = "\033[0;34m"  # blue
    elif type_value == "SPIRIT":
      color = "\033[0;35m"  # purple
    else:
      color = "\033[0m"     # normal

for name, value in mokebeast.items():
  print(f"{color}{name}: {value}")