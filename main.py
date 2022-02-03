import pygame

class Player:
    def __init__(self, song):
        self.song = song
        
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        
    def getstate(self):
       print(pygame.mixer.music.get_busy())
    
    def playsong(self):
        pygame.mixer.music.play()
        
    def pausesong(self):
        pygame.mixer.music.pause()
    
    def unpausesong(self):
        pygame.mixer.music.unpause()
    

pl1 = Player("Music/lofi.mp3",)




while True:
    user_input = input(">> ")
    if user_input == "go":
        pl1.playsong()
    elif user_input == "p":
        pl1.pausesong()
    elif user_input == "up":
        pl1.unpausesong()
    elif user_input == "state":
        pl1.getstate()
    elif user_input == "q":
        break
quit()