#!/usr/bin/env python
# -*- coding: utf-8 -*-
#:kivy 1.11.0

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout): # класс с относительным виджетом
    pass

class DrawingApp(App):# класс для вывода приложения
    def build(self): # функция для вывода приложения
        return DrawingSpace() # выодим класс с относительным виджетом

if __name__ == '__main__':
    DrawingApp().run()


