# -*- coding: utf-8 -*-
#mystruct.kv

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class MyGrapInst(RelativeLayout):
    pass

class MyStructApp(App):

    def build(self):
        return MyGrapInst()

if __name__ == "__main__":
    MyStructApp().run()


