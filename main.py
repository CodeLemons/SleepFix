import pygame

pygame.mixer.init()

pygame.mixer.Channel(0).play(pygame.mixer.Sound("Music/lofi.mp3"))
pygame.mixer.Channel(1).play(pygame.mixer.Sound("Music/rain.mp3"))
vol_list = list()
def volume_control(x, y):
    pygame.mixer.Channel(x).set_volume(y)
    print("Channel {x} volume set to {y}")
while True:
    user_input = input(">> ")
    if user_input == "p":
        pygame.mixer.Channel(0).pause()
        pygame.mixer.Channel(1).pause()
    elif user_input == "up":
        pygame.mixer.Channel(0).unpause()
        pygame.mixer.Channel(1).unpause()
    elif user_input == "state":
        pygame.mixer.Channel(0).get_busy()
        pygame.mixer.Channel(1).get_busy()
    elif user_input == "volume":
        ask = input("Enter (channel/volume): ")
        for i in ask.split("/"):
            vol_list.append(i)
        volume_control(int(vol_list[0]), float(vol_list[1]))
        vol_list.clear()
    elif user_input == "q":
        break
quit()
