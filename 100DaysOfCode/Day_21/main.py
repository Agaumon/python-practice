print("Math Game")
print("Let's see how well you know your times tables.")
number = int(input("Pick a number to multiply by: "))
count = 0
for i in range (1, 13):
  answer = int(input(f"{i} x {number} = "))
  if answer == i*number:
    print("Great work! Let's continue")
    count += 1
  elif answer != i*number:
    correct = i*number
    print("Nope. The answer was",correct)
  else:
    print("Incorrect response.")
    exit()
print("You scored",count,"out of",i)