print("List Generator")
start = int(input("Start at: "))
end = int(input("End at: "))
end += 1
inc = int(input("Increment between values: "))
for i in range(start, end, inc):
  print(i)