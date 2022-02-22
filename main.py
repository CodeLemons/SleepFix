from distutils.fancy_getopt import fancy_getopt
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import pygame

pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
pygame.mixer.init()
pygame.mixer.set_num_channels(10)

rainsound = pygame.mixer.Sound('Music/rainthunder.mp3')
firesound = pygame.mixer.Sound('Music/fireplace.mp3')
rainoncarsound = pygame.mixer.Sound('Music/rainoncar.mp3')
seawavessound = pygame.mixer.Sound('Music/seawaves.mp3')
windsound = pygame.mixer.Sound('Music/wind.mp3')
forestsound = pygame.mixer.Sound('Music/forest.mp3')
jazzsound = pygame.mixer.Sound('Music/jazz.mp3')
lofisound = pygame.mixer.Sound('Music/lofi.mp3')
tibetsound = pygame.mixer.Sound('Music/tibet.mp3')
crowdsound = pygame.mixer.Sound('Music/crowd.mp3')
rain_vol_list = list()
fire_vol_list = list()
rainoncar_vol_list = list()
seawaves_vol_list = list()
wind_vol_list = list()
forest_vol_list = list()
jazz_vol_list = list()
lofi_vol_list = list()
tibet_vol_list = list()
crowd_vol_list = list()
channel_one = pygame.mixer.Channel(0)
channel_two = pygame.mixer.Channel(1)
channel_three = pygame.mixer.Channel(2)
channel_four = pygame.mixer.Channel(3)
channel_five = pygame.mixer.Channel(4)
channel_six = pygame.mixer.Channel(5)
channel_seven = pygame.mixer.Channel(6)
channel_eight = pygame.mixer.Channel(7)
channel_nine = pygame.mixer.Channel(8)
channel_ten = pygame.mixer.Channel(9)

class FloatLayout(FloatLayout):
    pass

class SleepApp(App):

    def build(self):
        Window.size = (1024, 640)
        return FloatLayout()

    def rain(self):
            channel_one.play(rainsound, fade_ms=0, loops=-1)
            channel_one.set_volume(0.1)
            print("Rain sound started.")

    def rain_volume(self, *args):
        print(args[1])
        rain_vol_list.append(args[1])
        channel_one.set_volume(rain_vol_list.pop())
   
    def fire(self):
        channel_two.play(firesound, fade_ms=0, loops=-1)
        channel_two.set_volume(0.1)
        print("Fire Place sound started.")

    def fire_volume(self, *args):
        print(args[1])
        fire_vol_list.append(args[1])
        channel_two.set_volume(fire_vol_list.pop())
    
    def rainoncar(self):
        channel_three.play(rainoncarsound, fade_ms=0, loops=-1)
        channel_three.set_volume(0.1)
        print("Rain on car sound started.")

    def rainoncar_volume(self, *args):
        print(args[1])
        rainoncar_vol_list.append(args[1])
        channel_three.set_volume(rainoncar_vol_list.pop())

    def seawaves(self):
        channel_four.play(seawavessound, fade_ms=0, loops=-1)
        channel_four.set_volume(0.1)
        print("Sea Waves sound started.")

    def seawaves_volume(self, *args):
        print(args[1])
        seawaves_vol_list.append(args[1])
        channel_four.set_volume(seawaves_vol_list.pop())

    def wind(self):
        channel_five.play(windsound, fade_ms=0, loops=-1)
        channel_five.set_volume(0.1)
        print("Wind sound started.")

    def wind_volume(self, *args):
        print(args[1])
        wind_vol_list.append(args[1])
        channel_five.set_volume(wind_vol_list.pop())

    def forest(self):
        channel_six.play(forestsound, fade_ms=0, loops=-1)
        channel_six.set_volume(0.1)
        print("Forest sound started.")

    def forest_volume(self, *args):
        print(args[1])
        forest_vol_list.append(args[1])
        channel_six.set_volume(forest_vol_list.pop())

    def jazz(self):
        channel_seven.play(jazzsound, fade_ms=0, loops=-1)
        channel_seven.set_volume(0.1)
        print("Jazz sound started.")

    def jazz_volume(self, *args):
        print(args[1])
        jazz_vol_list.append(args[1])
        channel_seven.set_volume(jazz_vol_list.pop()) 

    def lofi(self):
        channel_eight.play(lofisound, fade_ms=0, loops=-1)
        channel_eight.set_volume(0.1)
        print("Lofi sound started.")

    def lofi_volume(self, *args):
        print(args[1])
        lofi_vol_list.append(args[1])
        channel_eight.set_volume(lofi_vol_list.pop())

    def tibet(self):
        channel_nine.play(tibetsound, fade_ms=0, loops=-1)
        channel_nine.set_volume(0.1)
        print("Tibetan gong sounds started")
    
    def tibet_volume(self, *args):
        print(args[1])
        tibet_vol_list.append(args[1])
        channel_nine.set_volume(tibet_vol_list.pop())
    
    def crowd(self):
        channel_ten.play(crowdsound, fade_ms=0, loops=-1)
        channel_ten.set_volume(0.1)
        print("Crowd sound started.")

    def crowd_volume(self, *args):
        print(args[1])
        crowd_vol_list.append(args[1])
        channel_ten.set_volume(crowd_vol_list.pop())




if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    SleepApp().run()