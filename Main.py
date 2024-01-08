from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from PIL import Image as PilImage
from io import BytesIO
from kivy.core.audio import SoundLoader
from random import randint
from kivy.uix.popup import Popup
from kivy.uix.label import Label
Builder.load_file('flapp.py')
