# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('mybox.kv')

class ComCreat(AnchorLayout):
    pass

class ComCreatApp(App):
    def build(self):
        return ComCreat()

if __name__ == '__main__':
    ComCreatApp().run()