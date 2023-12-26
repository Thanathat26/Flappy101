from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics.texture import Texture
Builder.load_file('flappy.kv')
class Background(Widget):
    texture = ObjectProperty(None)
    pass
class Gameflappy(App):
    def build(self):
        return Background()


if __name__ == '__main__':
    Gameflappy().run()