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

from peli.pelaajat import Pelaajat
from peli.lisaaKiihtyvyydet import LisaaKiihtyvyydet
from peli.velocityVerlet import VelocityVerlet
from pelilauta.seina import Seina
from pelilauta.reiat import Reiat
from pelilauta.pallot import Pallot
from pelilauta.lautadata import LautaData
from pelilauta.keppi import Keppi
from sys import exit
import time

lautadata = LautaData()

class Pelilauta(FloatLayout):
    hole_d = NumericProperty(lautadata.reianHalkaisija)
    max_y  = NumericProperty(lautadata.maxLautaY)
    def __init__(self, **kwargs):
        super(Pelilauta,self).__init__(**kwargs)



class E8ballGame(FloatLayout):
    lauta = ObjectProperty(None)
    #pallo = ObjectProperty(None)
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
            #x=pallo.getPalloX()
            #y=pallo.getPalloY()
            #print "x,y", x, y
            self.add_widget(pallo)
            #pallo.update_ellipse()
        #self.biljardipeli = Biljardipeli(self.pallot)
        #exit()
        self.keppi = Keppi()
        self.pelaajat = Pelaajat();
        self.lisaakiihtyvyydet = LisaaKiihtyvyydet();
        self.nopeusVerlet= VelocityVerlet(LautaData.dt);
        self.seina = Seina();
        self.reiat = Reiat();        
        self.jatka = False
        self.pallotliikkuu = True;        
        self.x1=0
        self.y1=0        
        self.x2=0
        self.y2=0
        print "INIT"

    def do_layout(self, *args):
        print "LAYOUT"
        for child in self.children:
            child.height = self.height
            child.width = self.width
        if (self.jatka):
            self.juokse()
            
    def on_size(self, *args):
        pass


    def on_pos(self, *args):
        pass
        #self.do_lay()

    def on_touch_up(self, touch):
        """ Ammutaan pallo liikkeelle """
        self.keppi.setPoikkeama(self.x1, self.y1, self.x2, self.y2)
        self.x1=0
        self.y1=0        
        self.x2=0
        self.y2=0
        for pallo in self.pallot.getPallotArray():
            pallo.setPalloVX(0.1)
            #y=pallo.getPalloY()
            #pallo.setPalloX(x+1e-3)        
        #self.keppi.iske(self.pallot.getLyontiPallo())
        #self.do_lay()
        print "SHOT"
        self.reiat.resetoiReiat()        
        self.jatka = True

    def on_touch_move(self, touch):
        #print "KEPPI: self.width, self.height",self.width, self.height
        #exit()
        touch.ud['x1'] = self.pallot.getLyontiPallo().getPalloX()*self.width
        touch.ud['y1'] = self.pallot.getLyontiPallo().getPalloY()*self.height
        self.x1 = touch.ud['x1']
        self.y1 = touch.ud['y1']
        touch.ud['x2'] = touch.x
        touch.ud['y2'] = touch.y
        self.x2 = touch.ud['x2']
        self.y2 = touch.ud['y2']
        pallo = self.pallot.getPallotArray()[1]
        #xx=pallo.getPalloX()
        #yy=pallo.getPalloY()
        #print "VALK x",xx
        #pallo.setPalloX(xx+0.1)
        #pallo.setPalloY(yy+0.1)

    def juokse(self):
        count = 0
        while (self.pallotliikkuu and self.jatka and count < 10):
            count = count + 1
            #self.pallot.update_child()
            #print "loopissa...",self.nopeusVerlet.getMaxSiirtyma(),self.pallot.suurinNopeus(), self.pallot.suurinKiihtyvyys(), self.pallot.getPallotArray()[2].x 
            self.pallot.nollaaKiihtyvyydet();
            print "before", self.pallot.getPallotArray()[0].x , self.pallot.getPallotArray()[0].y, self.pallot.getPallotArray()[0].vx , self.pallot.getPallotArray()[0].vy
            #self.lisaakiihtyvyydet.lisaaCoulombKiihtyvyydetBiljardiPallot(
            #    self.pallot);
            #self.lisaakiihtyvyydet.lisaaHardCoreKiihtyvyydet(self.pallot);
            #self.lisaakiihtyvyydet.lisaaKitka(self.pallot);
            self.nopeusVerlet.PaivitaVelocityVerlet(self.pallot);
            #print "after000", self.pallot.getPallotArray()[0].x , self.pallot.getPallotArray()[0].y
            #for pallo in self.pallot.getPallotArray():
            #    x=pallo.getPalloX()
            #    y=pallo.getPalloY()
            #    pallo.setPalloX(x+1e-2)
            #    pallo.setPalloY(y+1e-2)                
            print "after", self.pallot.getPallotArray()[0].x , self.pallot.getPallotArray()[0].y 
            self.seina.VaihdaLiikemaara(self.pallot);
            self.reiat.setEkanaReiassa(self.pallot);
            self.reiat.lisaaReikiinMenneet(self.pallot);            
            self.pelaajat.alkaakoYrittaaMustaa(self.reiat);
            self.reiat.tapaNormiPallot(self.pallot);

            self.jatka = self.reiat.tarkastaPallo(self.pallot.getMustaPallo());

            #time.sleep(1)
            #exit()
            if (not(self.reiat.tarkastaPallo(self.pallot.getLyontiPallo()
                                         ))):
                self.pallot.arvoLyontiPallonPaikka(0, 0, 
                    LautaData.MaxLautaX,LautaData.MaxLautaY, 
                    0.20);
                self.pallotliikkuu = False;
                self.pallot.nollaaNopeudet();
                # tutkitaan mitä tapahtui
                self.jatka = self.pelaajat.tarkastaTilanne(
                    self.reiat, self.pallot);                
            elif ((self.nopeusVerlet.getMaxSiirtyma() < LautaData.maxSiirtyma) 
                  and (self.pallot.suurinNopeus() < LautaData.maxNopeus)):
                self.pallotliikkuu = False
                self.pallot.nollaaNopeudet()
                self.nopeusVerlet.setMaxSiirtyma(1.0)
                # tutkitaan mitä tapahtui
                self.jatka = self.pelaajat.tarkastaTilanne(
                    self.reiat, self.pallot)
            #sys.exit()
        # nollataan reikien tilanne uutta lyöntiä varten
        self.jatka = self.pelaajat.tarkastaTilanne(self.reiat, self.pallot);

            

class E8ballApp(App):
    def build(self):
        game = E8ballGame()
        #game.set_biljardipeli(biljardipeli)
        #pelilauta.set_peli(biljardipeli)
        #game.set_pelilauta(pelilauta)
        Clock.schedule_interval(game.do_layout, 1.0 / 6.0)
        return game
        #return parent


if __name__ == '__main__':
    E8ballApp().run()
