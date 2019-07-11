# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('toolbox.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('comicwidgets.kv')

class ComicCreator(AnchorLayout): # создали клас ComicCreator наследовали от класса AnchorLayout(макет якорь)
    pass # здесь кода нет он в классе AnchorLayout

class ComicCreatorApp(App): # в данном классе говорится запустить класс
    def build(self):
        return ComicCreator() # запустить класс ComicCreator который запускает файл comiccreator.kv

if __name__ == '__main__':
    ComicCreatorApp().run()

# класс ComicCreatorApp загрузит comiccreator.kv автоматом то файл toolbox.kv
# нужно явно импортировать данный файл для этого импортируем from kivy.lang import Builder
# и загружаем файл явно Builder.load_file('toolbox.kv') теперь киви знает о нашем файле