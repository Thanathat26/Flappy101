from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
Builder.load_file('flappy.kv')
class Background(Widget):
    clound_texture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clound_texture = Image(source="cloud.png").texture
        self.clound_texture.wrap = 'repeat'
        self.clound_texture.uvisize = (Window.width)

    pass
class Gameflappy(App):
    def build(self):
        return Background()

if __name__ == '__main__':
    Gameflappy().run()