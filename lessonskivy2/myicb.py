# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
# myading.kv

class MyAddingIcb(RelativeLayout):
    pass

class MyAddingApp(App):
    def build(self):
        return MyAddingIcb()

if __name__ == "__main__":
    MyAddingApp().run()



