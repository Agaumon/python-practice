print("Exam Grade Calculator")
exam = input("Name of exam: ")
points = int(input("Maximum Possible Score: "))
score = int(input("Your score: "))
grade = score / points
letter = "N/A"
if grade >= 96:
  letter = "A+"
elif grade >= 93 and grade < 96:
  letter = "A"
elif grade >= 90 and grade < 93:
  letter = "A-"
elif grade >= 86 and grade < 90:
  letter = "B+"
elif grade >= 83 and grade < 86:
  letter = "B"
elif grade >= 80 and grade < 83:
  letter = "B-"
elif grade >= 76 and grade < 80:
  letter = "C+"
elif grade >= 70 and grade < 76:
  letter = "C"
elif grade >= 60 and grade < 70:
  letter = "D"
elif grade < 60:
  letter = "F"
grade = round(grade, 2)
print("You got",grade,"% which is a",letter)