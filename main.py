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
        #self.biljardipeli = Biljardipeli(self.pallot)
        self.keppi = Keppi()
        self.pelaajat = Pelaajat();
        self.lisaakiihtyvyydet = LisaaKiihtyvyydet();
        self.nopeusVerlet= VelocityVerlet(LautaData.dt);
        self.seina = Seina();
        self.reiat = Reiat();        
        self.shot = False
        self.jatka = True;       
        self.pallotliikkuu = True;        
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
            self.juokse()

    def juokse(self):

        while (self.jatka):
          # ammutaan lyöntipallo
          #setDelay(1);
          print "jatketaan...",self.nopeusVerlet.getMaxSiirtyma(),self.pallot.suurinNopeus()
          self.reiat.resetoiReiat();

          while (self.pallotliikkuu and self.jatka):
                #self.pallot.update_child()
                #print "loopissa...",self.nopeusVerlet.getMaxSiirtyma(),self.pallot.suurinNopeus(), self.pallot.suurinKiihtyvyys(), self.pallot.getPallotArray()[2].x 
                self.pallot.nollaaKiihtyvyydet();
                print "before", self.pallot.getPallotArray()[0].x , self.pallot.getPallotArray()[0].y 
                #self.lisaakiihtyvyydet.lisaaCoulombKiihtyvyydetBiljardiPallot(
                #    self.pallot);
                self.lisaakiihtyvyydet.lisaaHardCoreKiihtyvyydet(self.pallot);
                #self.lisaakiihtyvyydet.lisaaKitka(self.pallot);
                self.nopeusVerlet.PaivitaVelocityVerlet(self.pallot);
                print "after", self.pallot.getPallotArray()[0].x , self.pallot.getPallotArray()[0].y 
                self.seina.VaihdaLiikemaara(self.pallot);
                self.reiat.setEkanaReiassa(self.pallot);
                self.reiat.lisaaReikiinMenneet(self.pallot);            
                self.pelaajat.alkaakoYrittaaMustaa(self.reiat);
                self.reiat.tapaNormiPallot(self.pallot);
            
                self.jatka = self.reiat.tarkastaPallo(self.pallot.getMustaPallo());
            
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
        #Clock.schedule_interval(game.do_layout, 1.0 / 60.0)
        return game
        #return parent


if __name__ == '__main__':
    E8ballApp().run()
