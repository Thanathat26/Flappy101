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
Builder.load_file('flappy.kv')
class Background(Widget):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cloud_texture = Image(source="cloud1.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

        self.floor_texture = Image(source="floor.png").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

    def scroll_texture(self, time_passed):
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] + time_passed) % Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed) % Window.width, self.floor_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)
        texture = self.property('floor_texture')
        texture.dispatch(self)
    

class Gameflappy(App):
    def build(self):
        layout = FloatLayout()
        background = Background()
        layout.add_widget(background)
        Clock.schedule_interval(background.scroll_texture, 1/60.)
        return layout
    def create_pipe(self):
        pipe = Pipe()
        pipe.x = Window.width
        pipe.y = randint(50, Window.height - 50)
        self.root.add_widget(pipe)
        self.pipes.append(pipe)
    def update(self, dt):
        for pipe in self.pipes[:]:
            pipe.update()
            if pipe.right < 0:
                self.root.remove_widget(pipe)
                self.pipes.remove(pipe)
        if self.pipes and self.pipes[-1].x < Window.width - 200:
            self.create_pipe()
        
    
if __name__ == '__main__':
    Gameflappy().run()