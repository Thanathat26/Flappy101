from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.widget import Widget
Builder.load_file('flappy.kv')
class MyApp(Widget):
    pass
class Gameflappy(App):
    def build(self):
        return Gameflappy()
    
if __name__ == '__main__':
    Gameflappy().run()
    
    
