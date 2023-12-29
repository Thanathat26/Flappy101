# main.py

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
Builder.load_file('flappy.kv')
def collides(rect1,rect2):
    pass
class GameWidget(Widget):
    bird_pos = ObjectProperty((100, 200))
    enemy_pos = ObjectProperty((500, 200))
    enemy_speed = 600

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        self.sound = SoundLoader.load('CHIPI.mp3')
        self.sound.play()
        Clock.schedule_interval(self.move_step, 0)
        with self.canvas:
            self.bird = Rectangle(source='bird2.png', pos=self.bird_pos, size=(100, 100))
        self.create_enemy()
    def create_enemy(self):
        self.enemy_pos = (Window.width, randint(50, Window.height - 200))
        with self.canvas:
            self.enemy = Rectangle(source='rocket2.png', pos=self.enemy_pos, size=(100, 100))

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print('down', text)
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        print('up', text)
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def move_step(self, dt):
        cur_x = self.bird.pos[0]
        cur_y = self.bird.pos[1]
        step = 300 * dt
        if 'w' in self.pressed_keys:
            cur_y += step
        if 's' in self.pressed_keys:
            cur_y -= step
        if 'a' in self.pressed_keys:
            cur_x -= step
        if 'd' in self.pressed_keys:
            cur_x += step
        self.bird.pos = (cur_x, cur_y)
        self.enemy_pos = (self.enemy_pos[0] - self.enemy_speed * dt, self.enemy_pos[1])
        self.enemy.pos = self.enemy_pos

        if self.enemy_pos[0] < -100 or collides((self.bird_pos,self.bird.size),(self.enemy_pos,self.enemy.size)):
          print("Collision detected!")
          self.create_enemy()

class Background(Widget):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)
    bird_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cloud_texture = Image(source="cloud3.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

        self.floor_texture = Image(source="floor3.png").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

        self.bird_texture = Image(source='bird2.png').texture

    def scroll_texture(self, time_passed):
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] + time_passed) % Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed) % Window.width, self.floor_texture.uvpos[1])
        self.bird_texture.uvpos = ((self.bird_texture.uvpos[0] + time_passed) % Window.width, self.bird_texture.uvpos[1])
        texture = self.property('cloud_texture')
        texture.dispatch(self)
        texture = self.property('floor_texture')
        texture.dispatch(self)
        texture = self.property('bird_texture')
        texture.dispatch(self)

class Gameflappy(App):
    def build(self):
        layout = FloatLayout()
        background = Background()
        game_widget = GameWidget()
        layout.add_widget(background)
        Clock.schedule_interval(background.scroll_texture, 1/60.)
        layout.add_widget(game_widget)
        return layout

if __name__ == '__main__':
    Gameflappy().run()
