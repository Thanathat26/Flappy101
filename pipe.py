from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ObjectProperty,ListProperty
from kivy.uix.image import Image
class Pipe(Widget):
     Gap_size = NumericProperty(60)
     cap_size = NumericProperty(20)
     pipe_center = NumericProperty(0)
     bottom_body_position = NumericProperty(0)
     bottom_cap_position = NumericProperty(0)
     top_body_position = NumericProperty(0)
     top_cap_position = NumericProperty(0)
     pipe_body_texture = ObjectProperty
     lower_pipe = ListProperty((0,0,1,0,1,1,0,1))
     Top_pipe = ListProperty((0,0,1,0,1,1,0,1))
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pipe_body_texture = Image(source='pipe')
