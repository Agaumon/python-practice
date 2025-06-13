print("Conversion of years into total seconds")
years = int(input("How many years? "))
months = years * 12
print("There are",months,"months in",years,"years.")
days = years * 365
if years / 4 == 1:
  days = days + 1
print("There are",days,"days in",months,"months.")
hours = days * 24
print("There are",hours,"hours in",days,"days.")
minutes = hours * 60
print("There are",minutes,"minutes in",hours,"hours.")
seconds = minutes * 60
print("There are",seconds,"seconds in",minutes,"minutes.")