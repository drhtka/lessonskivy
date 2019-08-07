# -*- coding: utf-8 -*-

import math
from kivy.uix.togglebutton import ToggleButton

from kivy.graphics import Line
from comicwidgets1 import StickMan, DraggableWidget

class ToolButton(ToggleButton): # класс создавали ранее в toolbox.kv
    # начало работы касание,
    #  поэтому используем on_touch_down (мы его переопределяем)
    def on_touch_down(self, touch):
        # ds указываем где должно произойти событие
        # parent - указывает кто родитель
        ds = self.parent.drawing_space
        # state - кнопка нажата
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            # (x, y) - переводим абсолютные координаты в относительные
            (x, y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y) # будет рисовать, ещё не создан
            return True
        return super(ToolButton, self).on_touch_down(touch) # ссылаемся на ротильский класс

    def draw(self, ds, x, y):
        pass

class ToolStickman(ToolButton):
    def draw(self, ds, x, y):
        # создаём экземпляр класса StickMan
        sm = StickMan(width=48, heigth=48)


        # используем строку с класса ToolButton
        # (x, y) = ds.to_widget(touch.x, touch.y)
        # как счиытвать координаты
        sm.center = (x, y)

        # добавляем виджет
        ds.add_widget(sm) # куда добавить виджет

"""
нам нужно создать
class, который будет фиксировать динамические изменения
с методами:
1. рисования draw(), мы его просто переопределяем,
 он у нас вбит в класс ToolButton(ToggleButton)
2. обновления фигуры update_figure()
3. окончание рисования end_figure()
4. создания DraggableWidget() динамически, метод widgetize()
5. непоредственно создание фигуры create_figure()
6. добавление виджета create_widget()
примечания. пункты 5 и 6, мы просто впишем с pass(ничего не делать),
а в последствии в классах создания круга и линии переопределим.
"""

class ToolFigure(ToolButton):

    # переопреляем метод рисования
    def draw(self, ds, x, y): # функция с тремя артгументами
        """
        Переопределяем метод draw c класса ToolButton
        обратить внимание на параметры self, ds, x, y - ссылка на
        родителя и координаты 2D (x и y), но у нас она будет обозначать
        начало рисования: центр окружности, центр человечка, начало линиии.
        алгоритм:
        1. Определить систему координат
        2. Позаботиться что бы действие было выполнено в любом случае
        https://kivy.org/docs/api-kivy.graphics.html?highlight=canvas
        3. опредлить ссылку self.figure и указать систему координат и как изменять.
        4. указать, где (ds) рисовать и как(bind) - ds.bind,
         для рисования переопредлить стандартную функцию
        on_touch_move- движение.
        На вопрос, как рисовать вызываем функции обратного вызова, при помощи bind,
        как мы знаем функции обратного вызова используют другие функции,
         которые мы опишем позже,
        и будут фиксировать состояния в определённых точках
         update_figure - как обновлять фигуру
        end_figure - что понимать под окончанием рисования.


        """
        (self.ix, self.iy) = (x, y)# координаты
        with ds.canvas:
            self.figure=self.create_figure(x, y, x+1, y+1)# как рисовать
        ds.bind(on_touch_move=self.update_figure)# при помощи bind() связываем
        ds.bind(on_touch_up=self.end_figure)#

    def update_figure(self, ds, touch):
        # обновление фигуры
        if ds.collide_point(touch.x, touch.y): # считываем координаты
            (x,y)= ds.to_widget(touch.x, touch.y)# как обнавлять
            ds.canvas.remove(self.figure)# что удалить
            with ds.canvas: # что вместо этого сделать обязательно
                self.figure = self.create_figure(self.ix, self.iy, x, y)


    def end_figure(self, ds, touch):
        # определяем конечные точки рисования фигуры
        # определяем центр DraggableWidget() - сам метод напишем в widgetize()
        ds.unbind(on_touch_move=self.update_figure)
        ds.unbind(on_touch_up=self.end_figure)
        ds.canvas.remove(self.figure)
        # DraggableWidget()
        (fx, fy) = ds.to_widget(touch.x, touch.y)
        self.widgetize(ds, self.ix, self.iy, fx, fy)

    def widgetize(self, ds, ix, iy, fx, fy):
        # DraggableWidget динамически
        widget = self.create_widget(ix, iy, fx, fy)# создаём виджет
        # определяем соотношения координат 2 точки (ix, iy), что бы фигуру добавить в виджет
        (ix, iy) = widget.to_local(ix, iy, relative=True)
        # определяем соотношения координат 2 точки (fx, fy), что бы фигуру добавить в виджет
        (fx, fy) = widget.to_local(fx, fy, relative=True)
        widget.canvas.add(self.create_figure(ix, iy, fx, fy))# в виджет добавить фигуру
        ds.add_widget(widget)# добавить виджет к окну




    def create_figure(self, ix, iy, fx, fy):
        # создание фигуры переопределим в классах позже ToolCircle, ToolLine
        pass

    def create_widget(self, ix, iy, fx, fy):
        # создание виджета переопределим в классах позже ToolCircle, ToolLine
        pass


class ToolLine(ToolFigure):
    def create_figure(self, ix, iy, fx, fy):
        return Line(points=[ix,iy,fx,fy]) # обратите внимание вверху мы импортировали класс Line

    def create_widget(self, ix, iy, fx, fy):
        pos = (min(ix,fx), min(iy,fy))
        size = (abs(fx-ix), abs(fy-iy))
        return DraggableWidget(pos = pos, size=size)

class ToolCircle(ToolFigure):
    def create_figure(self, ix, iy, fx, fy):
        return Line(circle=[ix, iy, math.hypot(ix-fx,iy-fy)])
    def create_widget(self, ix, iy, fx, fy):
        r = math.hypot(ix-fx, iy-fy)
        pos = (ix-r, iy-r)
        size = (2*r, 2*r)
        return DraggableWidget(pos = pos, size = size)