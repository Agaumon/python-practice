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
def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    os.system("clear")
    print("Press P to Pause")
    print("Press M for main menu")
    option = input("Please select your choice: ")
    if option.upper() == "P":
      pause()
      break
    elif option.upper() == "M":
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
  print("Press 2 to Exit and Quit")
  main_option = int(input("Please select one of the options above: "))
  # take user's input
  if main_option == 1:
    play()
  elif main_option == 2:
    print("Goodbye!")
    pygame.quit()
    exit()
  else:
    print("Please enter a valid response.")
    continue
  # check whether you should call the play() subroutine depending on user's input
  if True:
    play()