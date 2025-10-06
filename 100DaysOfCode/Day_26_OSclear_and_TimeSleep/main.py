import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
def pause():
  pygame.mixer.pause()

pause()
def unpause():
  pygame.mixer.unpause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    os.system("clear")
    option = input("""
    Press P to Pause
    Press M for main menu
    """)
    if option.upper() == "P":
      pause()
      continue
    elif option.upper() == "M":
      pause()
      break
    else:
      print("Please enter a valid response.")
      continue
while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("Audio Player Main Menu")
  print("Press 1 to Play")
  print("Press 2 to Exit")
  main_option = input("Please select one of the options above: ")
  # take user's input
  if main_option == "1":
    play()
  elif main_option == "2":
    print("Goodbye!")
    pygame.quit()
    exit()
  else:
    print("Please enter a valid response.")
    time.sleep(1)
    continue
  # check whether you should call the play() subroutine depending on user's input