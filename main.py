total = 1000
interest = 0
for years in range (10):
  years += 1
  total += total * .05
  total = round(total,2)
  interest = total - 1000
  interest = round(interest,2)
  print("Year",years,"is",total )
print("You paid",interest,"in interest")