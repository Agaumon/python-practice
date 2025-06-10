print("Generation Indetifier by Birth Year")
born = int (input("What year were you born? "))
if born == 1883 or born <= 1900 & born > 1884:
  print("You've come a long way. A part of the Lost Generation, eh?")
elif born == 1901 or born <= 1927 & born > 1902:
  print("One of the greats! Born in the Greatest Generation")
elif born == 1928 or born <= 1945 & born > 1929:
  print("Shhh, you were born in the Silent generation")
elif born == 1946 or born <= 1964 & born > 1947:
  print("OOf, you're a part of the Baby Boomers")
elif born == 1965 or born <= 1980 & born > 1966:
  print("You're a part of Generation X")
elif born == 1981 or born <= 1996 & born > 1982:
  print("The most hated. You're a millenial")
elif born == 1997 or born <= 2012 & born > 1998:
  print("Just like me! Generation Z!")
elif born >= 2013:
  print("Don't let it get to your head. Generation Alpha")
else:
  print("You're either dead or don't exist yet")