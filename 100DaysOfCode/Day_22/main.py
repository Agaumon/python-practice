import random

print("Guess the Number Game: One to One Million")
number = random.randint(1,1000000)
count = 0
while True:
  answer = int(input("What is your guess? "))
  if answer != number:
    if answer < number and answer > 0:
      print("Number is too low. Try again")
      count += 1
    elif answer > number:
      print("Number is too high. Try again.")
      count += 1
    elif answer < 0:
      exit()
  elif answer == number:
    count += 1
    print("Good job! You got it right! You got it in",count,"tries.")
    exit()