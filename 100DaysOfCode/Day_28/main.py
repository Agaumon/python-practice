import os
import random
import time

print("Character Creator")

def rollDice(sides):
  while True:
    if sides > 1:
      return random.randint(1, sides)
    else:
      print("Not enough sides on this dice")

def healthRoll():
    health = ((rollDice(6) * rollDice(12))/2) + 10
    print("Health:",health)
    return health

def strengthRoll():
    strength = ((rollDice(6) * rollDice(12))/2) + 12
    print("Strength:",strength)
    return strength

def menu(Player):
  print(Player,"Character Creation")
  print("")
  name = input("Name your character: ")
  time.sleep(1)
  os.system("clear")
  
  while True:
    
    type = input("Please choose a race: Human, Elf, Orc, Dwarf: ").upper()
    
    if type == "HUMAN":
      type = "Human"
    
    elif type == "ELF":
      type = "Elf"
    
    elif type == "ORC":
      type = "Orc"
    
    elif type == "DWARF":
      type = "Dwarf"
    
    else:
      print("Please enter one of the listed races.")
      time.sleep(1)
      os.system("clear")
      continue
      
    while True:
      time.sleep(1)
      os.system("clear")
      print(name,"the",type)
      print()
      health = healthRoll()
      print()
      strength = strengthRoll()
      break
    break
  time.sleep(2)
  os.system("clear")
  return name, type, health, strength

def battle(player1_health,player2_health,player1_name,player2_name):
    
    player1_atk = rollDice(6)
    player2_atk = rollDice(6)
    
    if player1_atk < player2_atk:
      player1_health -= player2_atk
      print()
      print(player2_name,"hits",player1_name,"for",player2_atk)
      time.sleep(2)
      os.system("clear")
      
    elif player1_atk > player2_atk:
      player2_health -= player1_atk
      print()
      print(player1_name,"hits", player2_name, "for",player1_atk)
      time.sleep(2)
      os.system("clear")
    else:
      print()
      print("IT'S A TIE! The attacks cancel each other out")
      time.sleep(2)
      os.system("clear")
      
    return player1_health, player2_health

def game_loop():
  
  player1_name, player1_type, player1_health, player1_strength = menu("Player 1")
  player2_name, player2_type, player2_health, player2_strength = menu("Player 2")
  
  round = 1
  
  while True:
    print("ROUND",round,"FIGHT!")
    
    player1_health, player2_health = battle(player1_health, player2_health,player1_name,player2_name)

    print(player1_name,"HP:",player1_health)
    print()
    print(player2_name,"HP:",player2_health)
    
    if player1_health <= 0 and player2_health <= 0:
      print("It's a draw. Game Over")
      time.sleep(1)
      os.system("clear")
      break
      
    elif player1_health <= 0:
      print()
      print(player2_name,"has defeated",player1_name,"in",round,"rounds!")
      time.sleep(2)
      os.system("clear")
      break
      
    elif player2_health <= 0:
      print()
      print(player1_name,"has defeated",player2_name,"in",round,"rounds!")
      time.sleep(2)
      os.system("clear")
      break
      
    round += 1
    time.sleep(1)
    os.system("clear")
    
game_loop()