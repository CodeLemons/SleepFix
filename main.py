import pygame

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

vol_list = list()

def volume_control(x, y):
    pygame.mixer.Channel(x).set_volume(y)
    print("Channel " + str(x) + " volume set to " + str(y))
    
def master_volume(x):
    for i in range(8):
        pygame.mixer.Channel(i).set_volume(x)
        print("All channels have started on 20% volume.")

def sound_select(v):
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("Music/" + v + ".mp3"))
    
pygame.mixer.Channel(0).play(pygame.mixer.Sound("Music/lofi.mp3"))
pygame.mixer.Channel(1).play(pygame.mixer.Sound("Music/rain.mp3"))
pygame.mixer.Channel(2).play(pygame.mixer.Sound("Music/bells.mp3"))
pygame.mixer.Channel(3).play(pygame.mixer.Sound("Music/crowd.mp3"))
pygame.mixer.Channel(4).play(pygame.mixer.Sound("Music/waves.mp3"))
pygame.mixer.Channel(5).play(pygame.mixer.Sound("Music/firecrackle.mp3"))
pygame.mixer.Channel(6).play(pygame.mixer.Sound("Music/nightinsect.mp3"))
pygame.mixer.Channel(7).play(pygame.mixer.Sound("Music/sadmusic.mp3"))
master_volume(0.1)
          
while True:
    user_input = input(">> ")
    if user_input == "p":
        pygame.mixer.Channel(0).pause()
        pygame.mixer.Channel(1).pause()
        pygame.mixer.Channel(2).pause()
        pygame.mixer.Channel(3).pause()
        pygame.mixer.Channel(4).pause()
        pygame.mixer.Channel(5).pause()
        pygame.mixer.Channel(6).pause()
        pygame.mixer.Channel(7).pause()
    elif user_input == "up":
        pygame.mixer.Channel(0).unpause()
        pygame.mixer.Channel(1).unpause()
        pygame.mixer.Channel(2).unpause()
        pygame.mixer.Channel(3).unpause()
        pygame.mixer.Channel(4).unpause()
        pygame.mixer.Channel(5).unpause()
        pygame.mixer.Channel(6).unpause()
        pygame.mixer.Channel(7).unpause()
    elif user_input == "state":
        print(pygame.mixer.get_num_channels())
        pygame.mixer.Channel(0).get_busy()
        pygame.mixer.Channel(1).get_busy()
        pygame.mixer.Channel(2).get_busy()
        pygame.mixer.Channel(3).get_busy()
        pygame.mixer.Channel(4).get_busy()
        pygame.mixer.Channel(5).get_busy()
        pygame.mixer.Channel(6).get_busy()
        pygame.mixer.Channel(7).get_busy()
    elif user_input == "volume":
        ask = input("Enter (channel/volume): ")
        for i in ask.split("/"):
            vol_list.append(i)
        volume_control(int(vol_list[0]), float(vol_list[1]))
        vol_list.clear()
    elif user_input == "q":
        break
quit()
