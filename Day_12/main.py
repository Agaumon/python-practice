# Original Code to be Debugged
"""
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?)
ans1 = ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈
ans2 = input("Which lesson number is this?")
if(ans2>12):
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")
"""
#Code After being Debugged
print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?") #Was missing a quotation mark at the end.
ans1 = input("What language are we writing in? ") #There is no input request here even though it is asking a question and requiring an answer for the next few lines.
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈") #This line was missing a parentheses and a quotation mark at the end. Also the print statement was missing an indentation to align it to the else statement.
ans2 = int(input("Which lesson number is this? ")) #The answer for this input was being read as a string instead of what was expected in the next line as an integer.
if ans2 > 12:
  print("We're not quite that far yet")
elif(ans2==12): #Else-if statements must go before else statements.
  print("That's right!")
else:
  print("We've gone well past that!")