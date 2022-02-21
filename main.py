from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import pygame

pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
pygame.mixer.init()

rainsound = pygame.mixer.Sound('Music/rainthunder.mp3')
firesound = pygame.mixer.Sound('Music/fireplace.mp3')
rainoncarsound = pygame.mixer.Sound('Music/rainoncar.mp3')
seawavessound = pygame.mixer.Sound('Music/seawaves.mp3')
windsound = pygame.mixer.Sound('Music/wind.mp3')
rain_vol_list = list()
fire_vol_list = list()
rainoncar_vol_list = list()
seawaves_vol_list = list()
wind_vol_list = list()
channel_one = pygame.mixer.Channel(0)
channel_two = pygame.mixer.Channel(1)
channel_three = pygame.mixer.Channel(2)
channel_four = pygame.mixer.Channel(3)
channel_five = pygame.mixer.Channel(4)

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

        
    def fire(self):
        channel_two.play(firesound, fade_ms=0, loops=-1)
        channel_two.set_volume(0.1)
        print("Fire Place sound started.")
    
    def rainoncar(self):
        channel_three.play(rainoncarsound, fade_ms=0, loops=-1)
        channel_three.set_volume(0.1)
        print("Rain on car sound started.")

    def seawaves(self):
        channel_four.play(seawavessound, fade_ms=0, loops=-1)
        channel_four.set_volume(0.1)
        print("Sea Waves sound started.")

    def wind(self):
        channel_five.play(windsound, fade_ms=0, loops=-1)
        channel_five.set_volume(0.1)
        print("Wind sound started.")

    def rain_volume(self, *args):
        print(args[1])
        rain_vol_list.append(args[1])
        channel_one.set_volume(rain_vol_list.pop())

    def fire_volume(self, *args):
        print(args[1])
        fire_vol_list.append(args[1])
        channel_two.set_volume(fire_vol_list.pop())

    def rainoncar_volume(self, *args):
        print(args[1])
        rainoncar_vol_list.append(args[1])
        channel_three.set_volume(rainoncar_vol_list.pop())

    def seawaves_volume(self, *args):
        print(args[1])
        seawaves_vol_list.append(args[1])
        channel_four.set_volume(seawaves_vol_list.pop())

    def wind_volume(self, *args):
        print(args[1])
        wind_vol_list.append(args[1])
        channel_five.set_volume(wind_vol_list.pop())



if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    SleepApp().run()