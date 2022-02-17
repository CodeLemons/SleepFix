from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import pygame

pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
pygame.mixer.init()

rain = pygame.mixer.Sound('Music/rain.mp3')
bells = pygame.mixer.Sound('Music/bells.mp3')

class FloatLayout(FloatLayout):
    pass

class SleepApp(App):
    
    def build(self):
        Window.size = (800, 450)
        return FloatLayout()

    def rain(self):
        channel_one = pygame.mixer.Channel(0)
        channel_one.play(rain, fade_ms=700)
        print("Rain Button Pressed")
        
    def bells(self):
        channel_one = pygame.mixer.Channel(1)
        channel_one.play(bells, fade_ms=700)
        print("Bells Button Pressed")


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    SleepApp().run()