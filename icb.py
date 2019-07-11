# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
# Добавление изображения, цвета и фоны

# adding.kv

class AddingIcb(RelativeLayout):# возвращаем сам виджет относительный
    pass

class AddingApp(App):

    def build(self):
        return AddingIcb()

if __name__ == "__main__":
    AddingApp().run()


