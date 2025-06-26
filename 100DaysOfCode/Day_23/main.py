print("Login System")

def login():
  while True:
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user == "agaumon" and password == "password123":
      print("Login succesful.")
      break
    else:
      print("Incorrect username or password. Try again.")
      continue

login()