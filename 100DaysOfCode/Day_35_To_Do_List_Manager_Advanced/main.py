import os, time

print("To Do List Manager Pro")

toDoList = []

def colorChange(color):
  if color == "red":
    return "\033[0;31m"
  if color == "white":
    return "\033[1;37m"
  if color == "blue":
    return "\033[0;34m"
  if color == "green":
    return "\033[0;32m"
  if color == "yellow":
    return "\033[1;33m"
  if color == "origin":
    return "\033[0m"

reset = f"{colorChange('origin')}"
view = f"{colorChange('yellow')}view{reset}"
add = f"{colorChange('green')}add{reset}"
item = f"{colorChange('white')}item{reset}"
edit = f"{colorChange('blue')}edit{reset}"
remove = f"{colorChange('red')}remove{reset}"


def viewList():
  print()
  for item in toDoList:
    print(f"{item:^40}")
  print()

def clearList():
  while toDoList != []:
    toDoList.remove(toDoList[0])
    viewList()
    print()
    print("List cleared!")

def removeList():
  while True:
    remove = input(f"What item would you like to {colorChange('red')}remove?{reset} or would you like to {colorChange('red')}clear list?{reset} ")
    if remove == "clear list":
      clearList()
    else:
      if remove in toDoList:
        print()
        conRemove = input(f"Are you sure you want to remove {remove}?").lower()
        while True:
          if conRemove == "yes":
            toDoList.remove(remove)
            print()
            print(f"Successfully removed {colorChange('red')}{remove}{reset}")
            print()
            viewList()
            print()
            menu()
          else:
            break
  
def editList():
  viewList()
  item = input(f"What would you like to {colorChange('blue')}change?{reset} ")
  if item in toDoList:
    toDoList.remove(item)
    print()
    change = input(f"What would you like to {colorChange('blue')}change{reset} {item} to? ")
    if change in toDoList:
        print("Cannot have duplicates.")
    toDoList.append(change)
    print(f"You have successfully {colorChange('red')}removed{reset} {item} and added {change}.")
    viewList()

def addList():
  while True:
    newItem = input(f"What would you like to {add}? ")
    if newItem in toDoList:
      print()
      print(f"{colorChange('blue')}{newItem}{reset} is already on the list.")
      print()
      break
    else:  
      toDoList.append(newItem)
      print()
      print(f"You have added {newItem} to the list.")
      viewList()
      break
  
def menu():
  while True:
    request = input(f"Do you want to {view}, {add}, {remove} or {edit} the To Do list? ").upper()
    if request == "VIEW":
      viewList()
      continue
    elif request == "EDIT":
      editList()
      time.sleep(1)
      os.system("clear")
      continue
    elif request == "ADD":
      addList()
      time.sleep(1)
      os.system("clear")
      continue
    elif request == "REMOVE":
      removeList()
      time.sleep(1)
      os.system("clear")
      continue
    else:
      print()
      print(f"{colorChange('red')}{'Please add a valid response.'}{colorChange('white')}")
      time.sleep(.75)
      os.system("clear")
      continue

menu()