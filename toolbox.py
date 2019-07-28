# -*- coding: utf-8 -*-

import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from comicwidgets1 import StickMan, DraggableWidget

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x, y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        return super(ToolButton, self).on_touch_down(touch)
    def draw(self, ds, x, y):
        pass
"""

class ToolButton(ToggleButton):#создаем наследуемый класс который все знает про кнопки
    # нас интересует действие нажатие, пока не нажмем вторoй раз кнопка будет нажатой
    def on_touch_down(self, touch):# начало работы касание поэтому его перопределяем
        ds = self.parent.drawing_space# drawing_space будет родителем, рисовать будем вот на его пространстве
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):# если состояние == кнопки нажато и
    # на холсте родителе при помощи collide_point который определяет все координаты, рисуем объект с координатами (x, y)
    # параметр touch прикосновение об это зенает класс Motion Event - любой виджет всегда получает класс Motion Event
            (x, y) = ds.to_widget(touch.y, touch.y) # преобразовуем абсолютные координаты в относительные,
    # для атвоматического определения при рисовании
            self.draw(ds, x, y)# резервируем место при помощи self. и будующего метода который будет рисовать
    # (в пространстве, и на координатах которые определяет collide_point)
            return True# вернуть истину, разрешить действовать, в нашем случае рисовать
        return super(ToolButton, self).on_touch_down(touch)# все действия происходят в классе созданный в файле toolbox.kv
        # при помощи метода касания, котррый наследует все от класса ToggleButton для кнопок
    def draw(self, ds, x, y):# рисуем (в созданном пространстве, в определеных автоматом при косании на координатах)
        pass#говорим классу ничего не делать

"""# описание класса ToolButton