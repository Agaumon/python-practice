print("Star Wars Name Generator")

#Simple Version
print("Enter your first name, last name, mother's maiden name and the city you were born in: ")
name = input("> ").split()

firstName = name[0].capitalize()[0:3]
lastName = name[1].lower()[0:2]
maidName = name[2].capitalize()[0:2]
cityBorn = name[3].lower()[:3:-1][::-1]

fName = f"{firstName}{lastName}"
lName = f"{maidName}{cityBorn}"

print(f"{fName} {lName}")


# Extended Version
# firstName = input("Enter your first name: ").capitalize()
# firstName = firstName[0:3]
# print()

# lastName = input("Enter your last name: ").lower()
# lastName = lastName[0:2]
# print()

# maidName = input("Enter your mother's maiden name: ").capitalize()
# maidName = maidName[0:2]
# print()

# cityBorn = input("Ener the city you were born in: ").lower()
# cityBorn = cityBorn[:3:-1]
# cityBorn = cityBorn[::-1]
# print()

# fName = f"{firstName}{lastName}"
# lName = f"{maidName}{cityBorn}"
# print(f"{fName} {lName}")