from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
Builder.load_file('flappy.kv')
class Background(Widget):
    cloud_texture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cloud_texture = Image(source="cloud1.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)
    def scroll_texture(self, time_passed):
        print("scroll")

        pass
class Gameflappy(App):
    def build(self):
        return Background()
        Clock.schedule_interval(self.root.ids.background.scroll_texture , 1/2.)
    pass
if __name__ == '__main__':
    Gameflappy().run()