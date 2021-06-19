from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder

Window.size = (500, 700)
# Builder needed for loading kivy fle.
kv_file = Builder.load_file('design.kv')


class MyLayout(Widget):

    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def dot(self):
        prior = self.ids.calc_input.text
        if "." in prior:
            pass
        else:
            self.ids.calc_input.text = f'{prior}.'

    def math_sign(self,sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","+")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def equals(self):
        prior = self.ids.calc_input.text

        if "+" in prior:
            num_list = map(float, prior.split("+"))
            self.ids.calc_input.text = str(sum([i for i in num_list]))


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
