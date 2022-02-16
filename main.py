from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import pygame
import multiprocessing

import pygments

pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
pygame.mixer.init()

rain = pygame.mixer.Sound('Music/rain.mp3')
bells = pygame.mixer.Sound('Music/bells.mp3')

class SleepFix(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.window.add_widget(Image(source='Img/cloud.png'))
        
        self.button = Button(text='RAIN')
        self.button.bind(on_press=self.rain)
        self.window.add_widget(self.button)
       
        self.button = Button(text='BELLS')
        self.button.bind(on_press=self.bells)
        self.window.add_widget(self.button)

        return self.window


    def rain(self, instance):
        channel_one = pygame.mixer.Channel(0)
        channel_one.play(rain, fade_ms=500)
        print("Rain Button Pressed")
        
    def bells(self, instance):
        channel_one = pygame.mixer.Channel(1)
        channel_one.play(bells, fade_ms=500)
        print("Bells Button Pressed")

    # @staticmethod
    # def play_sound(sound, n):
        
if __name__ == '__main__':
    SleepFix().run()
