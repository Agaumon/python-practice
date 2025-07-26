# Contact Card
card = { "name" : "unknown",
        "dob" : "unknown",
        "number" : "unknown",
        "email" : "email",
        "address" : "unknown" }

name = input("Name: ")
card['name'] = name

DOB = input("Date of Birth: ")
card['dob'] = DOB

phone = input("Telephone number: ")
card['number'] = phone

email = input("Email: ")
card['email'] = email

address = input("Address: ")
card['address'] = address

print("\nHere's your contact card")
print(f"\nName: {card['name']}")
print(f"Date of Birth: {card['dob']}")
print(f"Telephone Number: {card['number']}")
print(f"Email: {card['email']}")
print(f"Address: {card['address']}")