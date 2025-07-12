print("What's Your Name?")

nameList = []

def printList():
  print()
  for name in nameList:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  nameFull = f"{firstName} {lastName}"
  if nameFull not in nameList:
    nameList.append(nameFull)
    printList()
  elif nameFull in nameList:
    print()
    print("Name already exists.")
    print()
    