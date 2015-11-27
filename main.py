# -*- coding: iso-8859-15 -*-
#from gwc_python.core import GestureWorksCore
#from gwc_python.GWCUtils import TOUCHREMOVED
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
#from kivy.properties import NumericProperty, ReferenceListProperty,\
#    ObjectProperty
#from kivy.vector import Vector
from kivy.graphics import *        
from kivy.clock import Clock
from peli.biljardipeli import Biljardipeli
from gui.piirtoalusta import PiirtoAlusta
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, BooleanProperty

from pelilauta.pallot import Pallot
from pelilauta.lautadata import LautaData
from pelilauta.keppi import Keppi
from sys import exit

lautadata = LautaData()

class Pelilauta(FloatLayout):
    hole_d = NumericProperty(lautadata.reianHalkaisija)
    max_y  = NumericProperty(lautadata.maxLautaY)
    def __init__(self, **kwargs):
        super(Pelilauta,self).__init__(**kwargs)

    def update_child(self):
        pass
        #print "ennen uodate_rect"
        #self.update_rect()



class E8ballGame(FloatLayout):
    lauta = ObjectProperty(None)
    #pallo = ObjectProperty(None)
    #keppi = ObjectProperty(None)
    #kuuntelija = ObjectProperty(None)
    x1 = NumericProperty()
    y1 = NumericProperty()
    x2 = NumericProperty()
    y2 = NumericProperty()

    def __init__(self, **kwargs):
        super(E8ballGame,self).__init__(**kwargs)
        self.pallot = Pallot()
        self.pelilauta = Pelilauta()
        for pallo in self.pallot.getPallotArray():
            print "ADDING BALL-WIDGET"
            self.add_widget(pallo)        
        self.biljardipeli = Biljardipeli(self.pallot)
        self.keppi = Keppi()
        self.shot = False
        self.x1=0
        self.y1=0        
        self.x2=0
        self.y2=0
        print "INIT"

    def do_layout(self, *args):
        for child in self.children:
            child.height = self.height
            child.width = self.width
        #    child.update_child()        

    def on_size(self, *args):
        self.do_layout()        
        #for child in self.children:
        #    child.height = self.height
        #    child.width = self.width
        #    child.update_child()


    def on_pos(self, *args):
        self.do_layout()

    def on_touch_up(self, touch):
        """ Ammutaan pallo liikkeelle """
        self.shot = True
        self.keppi.setPoikkeama(self.x1, self.y1, self.x2, self.y2)
        self.x1=0
        self.y1=0        
        self.x2=0
        self.y2=0
        self.keppi.iske(self.pallot.getLyontiPallo())
        self.update()


    def on_touch_move(self, touch):
        #print "KEPPI: self.width, self.height",self.width, self.height
        #exit()
        self.shot = False
        touch.ud['x1'] = self.pallot.getLyontiPallo().getPalloX()*self.width
        touch.ud['y1'] = self.pallot.getLyontiPallo().getPalloY()*self.height
        self.x1 = touch.ud['x1']
        self.y1 = touch.ud['y1']
        touch.ud['x2'] = touch.x
        touch.ud['y2'] = touch.y
        self.x2 = touch.ud['x2']
        self.y2 = touch.ud['y2']
        pallo = self.pallot.getPallotArray()[1]
        x=pallo.getPalloX()
        y=pallo.getPalloY()
        print "VALK x",x
        pallo.setPalloX(x+20)
        pallo.setPalloY(y+20)                        


        
    def update(self):
        print "update"
        self.do_layout()     
        print "SHOT????", self.shot
        if self.shot:
            self.shot = False
            self.biljardipeli.juokse()
        

class E8ballApp(App):
    def build(self):
        game = E8ballGame()
        #game.set_biljardipeli(biljardipeli)
        #pelilauta.set_peli(biljardipeli)
        #game.set_pelilauta(pelilauta)
        #Clock.schedule_interval(game.do_layout, 1.0 / 60.0)
        return game
        #return parent


if __name__ == '__main__':
    E8ballApp().run()
