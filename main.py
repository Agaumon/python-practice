import random, pprint

randomNumber = []

while len(randomNumber) < 9:
  number = random.randint(0,90)
  if number not in randomNumber:
    randomNumber.append(number)

randomNumber.sort()

my2DList = [ [randomNumber[0], randomNumber[1], randomNumber[2]],
             [randomNumber[3], "BINGO", randomNumber[4]],
             [randomNumber[5], randomNumber[6], randomNumber[7]]  ]

print("Ag's Bingo Card Generator")
pprint.pprint(my2DList)