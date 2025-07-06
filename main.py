def colorChange(color):
  if color == "red":
    return "\033[0;31m"
  if color == "white":
    return "\033[1;37m"
  if color == "blue":
    return "\033[0;34m"
  if color == "green":
    return "\033[0;32m"
  if color == "pink":
    return "\033[0;35m"
  if color == "origin":
    return "\033[1;33m"

title = (f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}={colorChange('origin')}Music App{colorChange('blue')}={colorChange('white')}={colorChange('red')}=")

print(f"{title:^90}")
print()
print(f"{colorChange('white')}{'Radio Gaga':>15}")
print(f"{colorChange('origin')}{'Queen':>10}")
print()
print()
print(f"{colorChange('white')}PREV")
print(f"{colorChange('green')}{'NEXT':>10}")
print(f"{colorChange('pink')}{'PAUSE':>18}")
print()

titleTwo = (f"{colorChange('white')}{'WELCOME TO':^40}\n"
            f"{colorChange('blue')}{'--   ARMBOOK   --':^40}\n"
            f"{colorChange('origin')}\n"
            f"{'Definitely not a rip off of':>35}\n"
            f"{'a certain other social':>35}\n{'networking site.':>35}"
            f"{colorChange('red')}\n{'Honest.':^40}\n"
            f"{colorChange('white')}") 

print(f"{titleTwo}\n")

username = "Username: "
password = "Password: "
login = (f"{colorChange('white')}{username:^40}\n" f"{colorChange('white')}{password:^40}")

print(login)
