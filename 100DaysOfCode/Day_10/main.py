print("Tip Calculator")
bill = int(input("How much was the bill? "))
tip = int(input("What percentage of tip would you like to tip? "))
tip = tip / 100
party = int(input("How many people are in your group? "))
total = int((bill + (bill * tip))) / party
total = round(total,2)
print("Your total for each of you is", total)