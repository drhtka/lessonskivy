# -*- coding: utf-8 -*-
#myscale.kv
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
#myscale.kv
from kivy.lang import Builder

Builder.load_file('myscaletwo.kv')

class MyDrawScale(RelativeLayout):
    pass

class MyScaleApp(App):

    def build(self):
        return MyDrawScale()

if __name__ == "__main__":
    MyScaleApp().run()