from kivy.app import App
import kivy.utils as utils
from kivy.graphics import Color, Rectangle

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import WindowBase

from Class import Window


def get_color(*args, test=False):
    if not test:
        color = (2.9 * args[0] / 255, 2.9 * args[1] / 255, 2.9 * args[2] / 255)
    else:
        color = (args[0] / 255, args[1] / 255, args[2] / 255)
    return color


class FirstScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.color = get_color(76, 188, 255)
        self.git_button = Button(text="Page Github", background_color=self.color, font_size=20,
                                 pos=(0, 0), size_hint=(0.2, .1))

        self.add_widget(self.git_button)


class Firetrack(App):

    def __init__(self):
        super(Firetrack, self).__init__()
        self.rect = None
        self.font_size = None
        self.color = get_color(76, 188, 255)

    def build(self):
        self.title = "Firetrack"
        WindowBase.minimum_height = 1000
        WindowBase.minimum_width = 1000
        self.root = root = FirstScreen()
        root.bind(size=self.update_size, pos=self.update_size)

        with root.canvas.before:
            Color(*get_color(76, 188, 255, test=True))
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def update_size(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos
        self.root.git_button.font_size = instance.size[0] / 40


if __name__ == "__main__":
    # Firetrack().run()
    window = Window("Firetrack", '#24A7A7', "480x360", (480, 360))
