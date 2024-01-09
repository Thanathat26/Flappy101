#mainขั้นกว่า
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from Flappy import Gameflappy

Builder.load_file('gameinterface.kv')

class Mylayout(Widget):
    pass

class Button1(App):
    def build(self):
        return Mylayout()
    def run_game(self):
        Clock.schedule_once(lambda dt: self.start_game(), 0)

    def start_game(self):
        Gameflappy().run()

if __name__ == '__main__':
    Button1().run()
