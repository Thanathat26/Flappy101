from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class Firstscreen(Screen):
    pass
class Seconscreen(Screen):
    pass
class Screenmamage(ScreenManager):
    pass
 
class Gameflappy(App):
    def build(self):
        Builder.load_file('flappy.kv')
        return ScreenManager()

if __name__ == '__main__':
    Gameflappy().run()
    
    
