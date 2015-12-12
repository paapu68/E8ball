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
            self.add_widget(pallo)
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

#    def do_layout(self, *args):
#        print "LAYOUT"
#        for child in self.children:
#            child.height = self.height
#            child.width = self.width
#        if (self.jatka):
#            self.juokse()
            
    def on_size(self, *args):
        pass


    def on_pos(self, *args):
        pass
        #self.do_lay()

    def on_touch_up(self, touch):
        """ Ammutaan pallo liikkeelle """
        self.keppi.setPoikkeama(self.x1, self.y1, self.x2, self.y2)
        self.keppi.setPoikkeama_x(self.x1, self.x2)
        self.keppi.setPoikkeama_y(self.y1, self.y2)                
        self.x1=0
        self.y1=0        
        self.x2=0
        self.y2=0
        self.keppi.iske(self.pallot.getLyontiPallo())
        print "SHOT"
        self.reiat.resetoiReiat()
        self.jatka = True
        #self.do_layout()
        #self.do_layout()
        

    def on_touch_move(self, touch):
        touch.ud['x1'] = self.pallot.getLyontiPallo().getPalloX()*self.width
        touch.ud['y1'] = self.pallot.getLyontiPallo().getPalloY()*self.height
        self.x1 = touch.ud['x1']
        self.y1 = touch.ud['y1']
        touch.ud['x2'] = touch.x
        touch.ud['y2'] = touch.y
        self.x2 = touch.ud['x2']
        self.y2 = touch.ud['y2']

    def do_layout(self, *args):
        for child in self.children:
            child.height = self.height
            child.width = self.width        
        count = 0
        if self.jatka:
            self.pallot.nollaaKiihtyvyydet();
            #self.lisaakiihtyvyydet.lisaaCoulombKiihtyvyydetBiljardiPallot(
            #    self.pallot);
            self.lisaakiihtyvyydet.lisaaHardCoreKiihtyvyydet(self.pallot);
            #self.lisaakiihtyvyydet.lisaaKitka(self.pallot);
            self.nopeusVerlet.PaivitaVelocityVerlet(self.pallot);
            self.seina.VaihdaLiikemaara(self.pallot);
            self.reiat.setEkanaReiassa(self.pallot);
            self.reiat.lisaaReikiinMenneet(self.pallot);            
            self.pelaajat.alkaakoYrittaaMustaa(self.reiat);
            self.reiat.tapaNormiPallot(self.pallot);

            self.jatka = self.reiat.tarkastaPallo(self.pallot.getMustaPallo());

            #self.do_layout()

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
            print "EXIT"

        
class E8ballApp(App):
    def build(self):
        game = E8ballGame()
        #game.set_biljardipeli(biljardipeli)
        #pelilauta.set_peli(biljardipeli)
        #game.set_pelilauta(pelilauta)
        Clock.schedule_interval(game.do_layout, 1/30)
        return game
        #return parent

if __name__ == '__main__':
    E8ballApp().run()
