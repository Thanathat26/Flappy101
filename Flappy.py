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
kv = Builder.load_file('flappy.kv')
class MyApp(Widget):
    pass 
class Gameflappy(App):
    def build(self):
        return Gameflappy(kv)
    
if __name__ == '__main__':
    Gameflappy().run()
    
    
