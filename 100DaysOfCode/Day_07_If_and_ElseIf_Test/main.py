print("""Fake Fan Finder
=============""")
faveshow = input("What is your favorite show?")
if faveshow == "Doctor who":
  yourdoctor = input("Who is your favorite Doctor?")
  if yourdoctor == "10":
    print("Not very original, but very fun doctor anyway")
  elif yourdoctor == "11":
    print("He's a fan favorite!")
  elif yourdoctor == "12":
    print("Oh? He's my favorite too!")
    favepisode = input("What's your favorite episode of 12's run?")
    if favepisode == "Hell bent":
      print("My favorite of all time.")
    elif favepisode == "When he regenerates":
      print("So he's not really your favorite, huh?")
    else:
      print("Always good because he was the best Doctor.")
  else:
    print("They were all good doctors, but just not a fan of them")
elif faveshow == "Supernatural":
  print("I've seen clips, not the entire show so meh")
else:
  print("Eh it's an alright choice I guess")