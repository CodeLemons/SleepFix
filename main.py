from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import pygame

pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
pygame.mixer.init()

rain = pygame.mixer.Sound('Music/rainthunder.mp3')
fire = pygame.mixer.Sound('Music/fireplace.mp3')
rainoncar = pygame.mixer.Sound('Music/rainoncar.mp3')
seawaves = pygame.mixer.Sound('Music/seawaves.mp3')
wind = pygame.mixer.Sound('Music/wind.mp3')

class FloatLayout(FloatLayout):
    pass

class SleepApp(App):
    
    def build(self):
        Window.size = (800, 450)
        return FloatLayout()

    def rain(self):
        channel_one = pygame.mixer.Channel(0)
        channel_one.play(rain, fade_ms=700)
        rain.set_volume(0)
        print("Rain sound started.")
        
    def fire(self):
        channel_one = pygame.mixer.Channel(1)
        channel_one.play(fire, fade_ms=700)
        fire.set_volume(0.3)
        print("Fire Place sound started.")
    
    def rainoncar(self):
        channel_one = pygame.mixer.Channel(2)
        channel_one.play(rainoncar, fade_ms=700)
        rainoncar.set_volume(0)
        print("Rain on car sound started.")

    def seawaves(self):
        channel_one = pygame.mixer.Channel(3)
        channel_one.play(seawaves, fade_ms=700)
        seawaves.set_volume(0)
        print("Sea Waves sound started.")

    def wind(self):
        channel_one = pygame.mixer.Channel(4)
        channel_one.play(wind, fade_ms=700)
        wind.set_volume(0)
        print("Wind sound started.")


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    SleepApp().run()