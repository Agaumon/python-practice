from getpass import getpass as input
print("Rock Paper Scissors Game")
print("Select your move: (R)ock, (P)aper, or (S)cissors? ")
P1score = 0
P2score = 0
while P1score < 3 and P2score < 3:
  Player1 = input("Player 1. Rock, Paper, or Scissors? ").upper()
  Player2 = input("Player 2. Rock, Paper, or Scissors? ").upper()
  # Normalize inputs to single letters
  if Player1 == ["ROCK", "ROCKS"]:
      Player1 = "R"
  elif Player1 == ["PAPER", "PAPERS"]:
      Player1 = "P"
  elif Player1 == ["SCISSORS", "SCISSOR"]:
      Player1 = "S"
  elif Player2 == ["ROCK", "ROCKS"]:
    Player2 = "R"
  elif Player2 == ["PAPER", "PAPERS"]:
    Player2 = "P"
  elif Player2 == ["SCISSORS", "SCISSOR"]:
    Player2 = "S"
  
  if Player1 == "R" and Player2 == "S": 
    print("Player 1 wins this round.")
    print("Rock crushes scissors.")
    P1score += 1
    continue
  elif Player1 == "S" and Player2 == "P":
    print("Player 1 wins this round.")
    print("Scissors cuts through paper.")
    P1score += 1
    continue
  elif Player1 == "P" and Player2 == "R":
    print("Player 1 wins this round.")
    print("Paper suffocates rock.")
    P1score += 1
    continue
  elif Player2 == "R" and Player1 == "S":
    print("Player 2 wins this round.")
    print("Rock crushes scissors.")
    P2score += 1
    continue
  elif Player2 == "S" and Player1 == "P":
    print("Player 2 wins this round.")
    print("Scissors cuts through paper.")
    P2score += 1
    continue
  elif Player2 == "P" and Player1 == "R":
    print("Player 2 wins this round.")
    print("Paper suffocates rock.")
    P2score += 1
    continue
  elif Player1 == Player2:
    print("It's a draw play again.")
    continue
  else:
    print("""That's not how you play rock paper scissors. 
    Please use R for rock, P for paper, and S for scissors as your inputs.""")
    continue
if P1score == 3:
  print("Player 1 wins!")
  exit()
elif P2score == 3:
  print("Player 2 wins.")
  exit()