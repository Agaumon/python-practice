import random

words = ["Doctor", "Who", "Rose", "Ood", "Donna", "Martha", "Dalek", "Cybermen", "Clara", "Regeneration"]

word = random.choice(words).lower()

tries = []
guessed = []

display = []
for letter in word:
  display.append("_")

print("Hangman!")

for symbol in display:
  print(symbol, end="")
print()

while "_" in display and len(tries) < 6:
  request = input("\nChoose a letter: ").lower()

  if request in guessed or request in tries:
    print("\nYou've already guessed this letter.")
    continue

  if request in word:
    print("\nCorrect!")
    for i in range(len(word)):
      if word[i] == request:
        display[i] = request
      guessed.append(request)
  else:
    print("\nIncorrect. Letter is not in word.")
    tries.append(request)
    print(f"\nYou have {6 - len(tries)} tries left.")

  for symbol in display:
    print(symbol, end="")
  print()

if "_" not in display:
  print(f"\nYou win. The word was: {word.capitalize()}")

else:
  print("\nYou lose.")
  exit()