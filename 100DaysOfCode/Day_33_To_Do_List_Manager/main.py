print("To Do List Manager")

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


def viewList():
  print()
  for item in toDoList:
    print(f"{item:^40}")
  print()

def editList():
  viewList()
  item = input(f"What would you like to {colorChange('blue')}change?{reset} ")
  if item.upper() == "REMOVE":
    remove = input(f"What item would you like to {colorChange('red')}remove?{reset} ")
    if remove in toDoList:
      toDoList.remove(remove)
      print(f"Successfully removed {colorChange('red')}{remove}{reset}")
  elif item in toDoList:
    toDoList.remove(item)
    print()
    change = input(f"What would you like to {colorChange('blue')}change{reset} {item} to? ")
    toDoList.append(change)
    print(f"You have successfully {colorChange('red')}removed{reset} {item} and added {change}.")
    viewList()

def addList():
    newItem = input(f"What would you like to {add}? ")
    toDoList.append(newItem)
    print(f"You have added {newItem} to the list.")
    viewList()

while True:
  request = input(f"Do you want to {view}, {add} or {edit} the To Do list? ").upper()
  if request == "VIEW":
    viewList()
    continue
  elif request == "EDIT":
    editList()
    continue
  elif request == "ADD":
    addList()
    continue
  else:
    print()
    print(f"{colorChange('red')}{'Please add a valid response.'}{colorChange('white')}")
    continue