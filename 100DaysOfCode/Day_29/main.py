def words(word,color):
  if color=="red":
    print("\033[31m", word, "\033[0m", sep="", end="")
  elif color=="blue":
    print("\033[0;34m", word, "\033[0m", sep="", end="")
  elif color=="green":
    print("\033[0;32m", word, "\033[0m", sep="", end="")
  elif color=="yellow":
    print("\033[1;33m", word, "\033[0m", sep="", end="")
  elif color=="purple":
    print("\033[0;35m", word, "\033[0m", sep="", end="")
  else:
    print(word,end="")

print("Super Subroutine")
print("With my ", end="")
words("new program ", "red")
print("I can just call ", end="")
words("red ","yellow")
print("and that word will appear in the ",end="")
words("color ","green")
print("I ",end="")
words("set it to","blue")
print()
print("With no ",end="")
words("weird gaps.", "purple")
print()
words("E","red")
words("p","yellow")
words("i","green")
words("c","blue")
words(".","purple")