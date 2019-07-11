# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout#относительно виджет

class GraphicInstr(RelativeLayout):
    pass

class StructurApp(App):#этот класс возвращает виджет

    def build(self):
        return GraphicInstr()#вот здесь

if __name__ == "__main__":
    StructurApp().run()


