from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
Builder.load_file('flappy.kv')
class Background(Widget):
    pass
class Gameflappy(App):
    pass


if __name__ == '__main__':
    Gameflappy().run()