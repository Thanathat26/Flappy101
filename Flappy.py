from kivy.app import App
from kivy.lang import Builder

Builder.load_file('flappy.kv')

class Gameflappy(App):
    def build(self):
        return Builder.load_file('flappy.kv')

if __name__ == '__main__':
    Gameflappy().run()
