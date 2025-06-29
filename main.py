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
    input()
while True:
  # clear the screen 
  # Show the menu
  # take user's input
  # check whether you should call the play() subroutine depending on user's input
  if True:
    play()