from asyncio import start_server
from concurrent.futures import thread
import time
import multiprocessing
import audioplayer

class Player:
    def __init__(self, **kwargs):
        # Shared Variable.
        self.play = True
        self.thread_kill = False
    
    def start_sound(self):
        while True and not self.thread_kill:
            if self.play == True:
                audioplayer.AudioPlayer("Music/lofi.mp3").play(block=True)
    
    def stop_sound(self):
        pass

    def start_thread(self):
        self.play = True
        p1 = multiprocessing.Process(name="thread1", target=start_sound)
        p1.start()
        p1.join()
        
    def run(self):
        user_input = input(">> ")
        if user_input == "p":
            self.start_thread()
            

p2 = Player()
p2.run()
        