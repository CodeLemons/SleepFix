import pygame

pygame.mixer.init()

pygame.mixer.music.load("Music/lofi.mp3")


while True:
    user_input = input(">> ")
    if user_input == "go":
        pygame.mixer.music.play()
    elif user_input == "p":
        pygame.mixer.music.pause()
    elif user_input == "up":
        pygame.mixer.music.unpause()
    elif user_input == "q":
        break
quit()