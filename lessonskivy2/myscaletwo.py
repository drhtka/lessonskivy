# -*- coding: utf-8 -*-
#/myscaletwo.kv
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class MyScaleTwo(RelativeLayout):
    pass

class MyScaleTwoApp(App):
    def build(self):
        return MyScaleTwo()

if __name__ == "__main__":
    MyScaleTwoApp().run()


