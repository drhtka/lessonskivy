# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout


class DrawingScale(RelativeLayout):
    pass

class ScaleApp(App):
    def build(self):
        return DrawingScale()

if __name__ == "__main__":
    ScaleApp().run()


