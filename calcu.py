from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the initial size of the window
Window.size = (500, 700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"
    def button_press(self,button):
        prior = self.ids.calc_input.text
        if prior == "Error":
            self.ids.calc_input.text =" "
            self.ids.calc_input.text = f'{button}'
        elif prior == "0":
            self.ids.calc_input.text =" "
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f"{prior}{button}"
    def p_s(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
             self.ids.calc_input.text = f'{-int(prior)}'

    def dot(self):
        prior = self.ids.calc_input.text
        if "+" in prior:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass  
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior


    def Math_sight(self,sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text =f"{prior}{sign}"
    
    def equals(self):
        prior = self.ids.calc_input.text
        try:
             answer = eval(prior)
             self.ids.calc_input.text=str(answer)
        except:
            self.ids.calc_input.text=("Error")
        '''if "+" in prior:
            num_list = prior.split("+")
            count = 0.0
            for n in num_list and "." not in num_list[-1]:
                count = count + float(n)
            self.ids.calc_input.text = str(count)
        '''


class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()
