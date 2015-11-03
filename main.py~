# -*- coding: iso-8859-15 -*-
#from gwc_python.core import GestureWorksCore
#from gwc_python.GWCUtils import TOUCHREMOVED
from kivy.app import App
from kivy.uix.widget import Widget
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

lautadata = LautaData()
class Pelipallot(Widget, Pallot):
    def __init__(self, **kwargs):
        super(Pelipallot, self).__init__(**kwargs)
        self.pallot = []
        self.asetaPallojenAlkupaikat()
        self.asetaPallojenPerusVaraus(100)
        self.asetaPallojenVaraukset()
        self.asetaPallojenVarit()
        self.update()
        self.bind(pos=self.update, size=self.update)

    def update(self,*args):
        #piirretaan pallot
        import sys
        #print "self.pallot", self.pallot
        self.canvas.clear()
        d=lautadata.pallonHalkaisija*self.width
        with self.canvas:
            for pallo in self.getPallotArray():
                vari = pallo.getPalloVari()
                #print "vari", vari
                if vari == "valkoinen":
                    Color(1, 1, 1)
                elif vari == "musta":
                    Color(0, 0, 0)
                elif  vari == "punainen":
                    Color(1, 0, 0)
                elif  vari == "sininen":
                    Color(0, 0, 1)
                else:
                    print "COLOR NOT FOUND"
                    sys.exit()
                #sys.exit()                
                print "plotting", pallo.getPalloX(),self.width
                self.ellipse = \
                               Ellipse(pos=(pallo.getPalloX()*
                                            self.width - d / 2, 
                                            pallo.getPalloY()*
                                            self.height - d / 2), 
                                       size=(d, d))

#    def aseta_pallot(self, pallot):
#        self.pallot = pallot

#    def get_pallot(self):
#        return self.pallot


class Pelilauta(Widget):
    hole_d = NumericProperty(lautadata.reianHalkaisija)
    max_y  = NumericProperty(lautadata.maxLautaY)
    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)

    def update(self):
        print "ennen uodate_rect"
        #self.update_rect()



class E8ballGame(Widget):
    lauta = ObjectProperty(None)
    #keppi = ObjectProperty(None)
    #kuuntelija = ObjectProperty(None)
    x1 = NumericProperty()
    y1 = NumericProperty()
    x2 = NumericProperty()
    y2 = NumericProperty()

    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        self.pelilauta = Pelilauta()
        self.pelipallot = Pelipallot()
        print self.pelipallot
        #exit()
        self.biljardipeli = Biljardipeli(self.pelipallot)
        self.keppi = Keppi()
        self.shot = False
        self.x1=0
        self.y1=0        
        self.x2=0
        self.y2=0

#    def get_pallot(self):
#        return self.pallot

    def on_touch_up(self, touch):
        """ Ammutaan pallo liikkeelle """
        self.shot = True
        self.keppi.setPoikkeama(self.x1, self.y1, self.x2, self.y2)
        self.x1=0
        self.y1=0        
        self.x2=0
        self.y2=0
        self.keppi.iske(self.pelipallot.getLyontiPallo())


    def on_touch_move(self, touch):
        self.shot = False
        touch.ud['x1'] = self.pelipallot.getLyontiPallo().getPalloX()*self.width
        touch.ud['y1'] = self.pelipallot.getLyontiPallo().getPalloY()*self.height
        self.x1 = touch.ud['x1']
        self.y1 = touch.ud['y1']
        touch.ud['x2'] = touch.x
        touch.ud['y2'] = touch.y
        self.x2 = touch.ud['x2']
        self.y2 = touch.ud['y2']
        
    def update(self, dt):
        #pass
        self.pelipallot.update()
        print "SHOT????", self.shot
        if self.shot:
            self.shot = False
            self.biljardipeli.juokse()
        #print "self.pallot", self.pallot
        #for pallo in self.pallot.getPallotArray():
        #    print pallo.getPalloX()
        #self.pelilauta.aseta_pallot(self.get_pallot())
        #self.pelipallot.update()
        

class E8ballApp(App):
    def build(self):
        game = E8ballGame()
        #game.set_biljardipeli(biljardipeli)
        #pelilauta.set_peli(biljardipeli)
        #game.set_pelilauta(pelilauta)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
        #return parent


if __name__ == '__main__':
    E8ballApp().run()
