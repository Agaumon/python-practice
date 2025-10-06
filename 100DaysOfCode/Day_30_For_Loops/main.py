print("30 Days Down - How does it feel?")
for i in range(1, 30):
  print(f"Day {i}")
  response = input("> ")
  print(f"{f'You thought Day {i} was':^40}")
  print(f"{response:^40}")