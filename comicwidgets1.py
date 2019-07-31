# -*- coding: utf-8 -*-
#comicwidgets.kv

from kivy.properties import ListProperty, NumericProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line, Color
#from kivy.graphics import *
#from kivy.graphics import Color
#from random import random as r

class DraggableWidget(RelativeLayout):
    def __init__(self, **kwargs):
        self.selected = None
        super(DraggableWidget, self).__init__(**kwargs)

    def  on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.select()
            #self.select_color()
            return True
        return super(DraggableWidget, self).on_touch_down(touch)

    def select(self,):
        if not self.selected:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                #Color(rgb=(1, 0, 0))
                #self.selected = Color(1, 1, 1)
                self.selected = Line(restangle=(0,0,self.width,self.height), dash_offset=2)

    def on_touch_move(self, touch):
        (x,y) = self.parent.to_parent(touch.x, touch.y)
        if self.selected and self.parent.collide_point(x - self.width/2, y - self.height/2):
            go = self.parent.general_options
            go.translation=(touch.x-self.ix,touch.y-self.iy)
            return True
        return super(DraggableWidget, self).on_touch_move(touch)

    def translate(self, x, y):
        self.center_x = self.ix + x
        self.center_y = self.iy = self.iy + y

    def on_touch_up(self, touch):
        if self.selected:
            self.unselect()
            return True
        return super(DraggableWidget, self).on_touch_up(touch)

    def unselect(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected = None

    #def select_color(self,):
     #   if not self.selected:
      #      with self.canvas:
       #         Color(1, 1, 1)
        #        d = 30.0
         #   return True

class StickMan(DraggableWidget):
    pass
