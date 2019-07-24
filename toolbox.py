# -*- coding: utf-8 -*-

import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from comicwidgets1 import StickMan, DraggableWidget

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):#касание
        ds = self.parent.drawing_space# ds просто переменная
        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            (x, y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        return super(ToolButton, self).on_touch_down(touch)
    def draw(self, ds, x, y):
        pass


