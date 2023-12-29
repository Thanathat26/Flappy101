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
from random import randint
from pipe import Pipe
Builder.load_file('flappy.kv')
class Background(Widget):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cloud_texture = Image(source="cloud3.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

        self.floor_texture = Image(source="floor3.png").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width / self.cloud_texture.width, -1)


    def scroll_texture(self, time_passed):
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] + time_passed) % Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed) % Window.width, self.floor_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)
        texture = self.property('floor_texture')
        texture.dispatch(self)

class Bird(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "bird1.png"
        self.size_hint = (None, None)
        self.size = (250, 250)
        self.pos = (100, 200)
        self.velocity_y = 0

    def update(self, dt):
        self.velocity_y -= 500 * dt  
        self.y += self.velocity_y * dt

        if self.top > self.parent.top:
            self.top = self.parent.top
            self.velocity_y = 0
class Gameflappy(App):
    pipes = []
    def build(self):
        layout = FloatLayout()
        self.bird = Bird()
        background = Background()
        layout.add_widget(background)
        layout.add_widget(self.bird)
        Clock.schedule_interval(background.scroll_texture, 1/60.)
        return layout
    def start_game(self):
        num_pipes = 5
        distance_between_pipes = Window.width / (num_pipes - 1)
        for i in range (num_pipes):
            pipe = Pipe()
            pipe.pipe_center = randint(96 + 100, self.root.height - 100)
            pipe.pos = (Window.width + i*distance_between_pipes,96)
            pipe.size
            self.pipes.append(pipe)
            self.root.add_widget(pipe)
if __name__ == '__main__':
    Gameflappy().run()