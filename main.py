print("Positivity or Insult Genrator")

name = input("What is your name? ")

day = input("What day is today? ")

favFood = input("What's your favorite food? ")

activity = input("What's your favorite thing to do? ")

feeling = input("How are you feeling today? ")

if name == "Miguel" or name == "miguel":
  print("Hey buddy! Nice to see you on this fine ",day,".")
elif name == "Kenneth" or name == "kenneth":
  print("What's up my guy? What're we doing on this fine ",day,"?")
else:
  print("Hello there stranger! Isn't this a fine",day,"?")
if day == "Friday" or day == "friday":
  print("What a great way to start the weekend with this code.")
elif day == "Saturday" or day == "saturday":
  print("Halfway through the weekend. Kinda sucks, right?")
elif day == "Monday" or day == "monday":
  print("It can't be that great, right? It's a Monday and we hate Mondays.")
else:
  print("Just another day, another dollar.")
if feeling == "good" or feeling == "Good":
  ask = input("Feeling up for a joke/insult or need an upper? ")
  if ask == "joke" or ask == "Joke" or ask == "insult" or ask == "Insult":
    print("Alright. You asked for it so here it comes.")
    print("You like to",activity,",but you're not the greatest at it. Get better.")
    print("Your favorite food is",favFood,"""Well you're starting to look like one too.
It's time to hit the gym.""")
  elif ask == "upper" or ask == "Upper":
    print("Alright, my friend. I hope this makes your day.")
    print("""You're an amazing person and do so much for everyone else. 
    Take the load off and stuff your face with""",favFood,
    "You deserve to enjoy your day and",activity,
    """. So just chill this""",day)
  else:
    print("Well I guess either way, I hope you're day is going okay...baka")