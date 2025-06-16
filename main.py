from getpass import getpass as input
print("Rock Paper Scissors Game")
print("Select your move: (R)ock, (P)aper, or (S)cissors? ")
Player1 = input("Player 1. Rock, Paper, or Scissors? ")
Player2 = input("Player 2. Rock, Paper, or Scissors? ")
if Player1 == "R" and Player2 == "S" or Player1 == "rock" and Player2 == "scissors": 
  print("Player 1 wins")
  print("Rock crushes scissors.")
elif Player1 == "S" and Player2 == "P":
  print("Player 1 wins")
  print("Scissors cuts through paper.")
elif Player1 == "P" and Player2 == "R":
  print("Player 1 wins")
  print("Paper suffocates rock.")
elif Player2 == "R" and Player1 == "S":
  print("Player 2 wins")
  print("Rock crushes scissors.")
elif Player2 == "S" and Player1 == "P":
  print("Player 2 wins")
  print("Scissors cuts through paper.")
elif Player2 == "P" and Player1 == "R":
  print("Player 2 wins")
  print("Paper suffocates rock.")
elif Player1 == "R" and Player2 == "R" or Player1 == "S" and Player2 == "S" or Player1 == "P" and Player2 == "P":
  print("It's a draw play again.")
else:
  print("That's not how you play rock paper scissors. Please use R for rock, P for paper, and S for scissors as your inputs.")