from email.mime import audio
import multiprocessing
from playsound import playsound
import audioplayer
import threading

class MusicPlayer:
    def __init__(self, songs):
        self.all_songs = songs

    
    def select_song(self, song):
       #threading.Thread(audioplayer.AudioPlayer(song).play()).start()
       audioplayer.AudioPlayer(song).play()



    def start_song(self, song_name):
        # Check if song in list
        self.select_song(song_name)
        #process = multiprocessing.Process(target=MusicPlayer.select_song(song_name))
        # save process in class dict
        
        print("Process started")
    
    @staticmethod
    def stop_song(process):
        process.terminate()
        print("Process terminated")

if __name__ == '__main__':
    songs = ["lofi.mp3", "rain.mp3", "bells.mp3"]
    p = MusicPlayer(songs)
    while True:
        u_input = input(">> ")
        chosen_song = u_input
        p.start_song(u_input)
        if u_input == "q":
            p.stop_song(chosen_song)
        
