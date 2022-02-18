from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import pygame
kv = Builder.load_string("""
<MyGrid>
    slider: slider
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: str(slider.value)
        Slider:
            id: slider
            min: 0.000
            max: 1.000
            orientation: 'horizontal'
        Button:
            text: "Play Song"
            on_press: root.btn()
""")
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
pygame.mixer.init()
rain = pygame.mixer.Sound('Music/rainthunder.mp3')
class MyGrid(BoxLayout):
    slider = ObjectProperty()
    def btn(self):
        return self.slider.value

    def volume(self):    
        channel_one = pygame.mixer.Channel(0)
        channel_one.play(rain, fade_ms=0, loops=-1)
        rain.set_volume(self.slider.value)


class MyApp(App, MyGrid):
    def build(self):
        print(self.btn())
        return MyGrid()
if __name__ == '__main__':
    MyApp().run()