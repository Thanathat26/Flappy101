#mainขั้นกว่า
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
Builder.load_file('Flappy.kv')




if __name__ == '__main__':
    FlappyApp().run()