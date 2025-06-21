print("Guess the Number Game")
number = 413000
count = 0
while True:
  answer = int(input("What is your guess? "))
  if answer != number:
    if answer < number:
      print("Number is too low. Try again")
      count += 1
    elif answer > number:
      print("Number is too high. Try again.")
      count += 1
  elif answer == number:
    count += 1
    print("Good job! You got it right! You got it in",count,"tries.")
    exit()
  elif answer < 0:
    exit()