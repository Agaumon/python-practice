
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
        user_input = input("Press 'p' to pause, 'm' for main menu: ")
        if user_input.lower() == 'p':
            pause()
            break
        elif user_input.lower() == 'm':
            break

while True:
    # clear the screen 
    os.system('clear')
    
    # Show the menu
    print("🎵 Audio Player Menu 🎵")
    print("1. Play")
    print("2. Pause")
    print("3. Quit")
    
    # take user's input
    choice = input("Enter your choice (1-3): ")
    
    # check whether you should call the play() subroutine depending on user's input
    if choice == "1":
        play()
    elif choice == "2":
        pause()
    elif choice == "3":
        print("Goodbye!")
        pygame.quit()
        break
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
