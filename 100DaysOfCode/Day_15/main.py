print("Animal Sound Loop")
exit = "NO"
while exit != "YES":
    animal = input("What animal do you want? ").upper()

    if animal == "COW":
        print("The cow goes moo.")
    elif animal == "CHICKEN":
        print("The chicken goes caw.")
    elif animal == "PIG":
        print("The pig goes oink.")
    elif animal == "DUCK":
        print("The duck goes quack.")
    else:
        print("Not a valid input or not an animal we have stored.")

    exit = input("Exit? ").upper()
    if exit != "YES":
        print("Next animal.")