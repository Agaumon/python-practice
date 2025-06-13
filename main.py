print("Generation Indetifier by Birth Year")
born = int (input("What year were you born? "))
if born >= 1883 and born <= 1900:
  print("You've come a long way. A part of the Lost Generation, eh?")
elif born >= 1901 and born <= 1927:
  print("One of the greats! Born in the Greatest Generation")
elif born >= 1928 and born <= 1945:
  print("Shhh, you were born in the Silent generation")
elif born >= 1946 and born <= 1964:
  print("OOf, you're a part of the Baby Boomers")
elif born >= 1965 and born <= 1980:
  print("You're a part of Generation X")
elif born >= 1981 and born <= 1996:
  print("The most hated. You're a millenial")
elif born >= 1997 and born <= 2012:
  print("Just like me! Generation Z!")
elif born >= 2013:
  print("Don't let it get to your head. Generation Alpha")
else:
  print("You're either dead or don't exist yet")