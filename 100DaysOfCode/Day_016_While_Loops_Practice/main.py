print("Fill-in the Blank lyrics")
print("Try your best to enter the correct word for the lyrics")
counter = 0
while True :
  print("Burning photos had to learn to ___ __")
  lyrics = input("Fill in the blanks: ").lower()
  print("Try again.")
  counter += 1
  if lyrics == "let go":
    print("Well done, you got it in",counter,"attempts!")
    break