import os
import time


listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("listOfEmail")
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter += 1
  time.sleep(1)

def spam():
  count = 0
  for email in listOfEmail:
    if count <= 10:
      os.system("clear")
      time.sleep(1)
      print(f"""Dear {email}
    It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.Love and hugs,
    Ian Spammington III""")
    time.sleep(1)
  
while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu== "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spam()
  time.sleep(1)
  os.system("clear")