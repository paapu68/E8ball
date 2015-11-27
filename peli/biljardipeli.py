# -*- coding: iso-8859-15 -*-
"""
 * Biljardipelin pyörityslogiikkaa, lisäksi metodit joilla saadaan
 * kaivettua pelin osia.
"""
from pelaajat import Pelaajat
from peli.lisaaKiihtyvyydet import LisaaKiihtyvyydet
from pelilauta.lautadata import LautaData
from peli.velocityVerlet import VelocityVerlet
from pelilauta.seina import Seina
from pelilauta.reiat import Reiat
from pelilauta.keppi import Keppi
from pelilauta.pallot import Pallot
from gui.piirtoalusta import PiirtoAlusta
from kivy.uix.widget import Widget
#from pelaaja import Pelaaja

class Biljardipeli(Widget):
    def __init__(self, pallot):
        super(Biljardipeli, self).__init__()
        self.pelaajat = Pelaajat();
        self.lisaakiihtyvyydet = LisaaKiihtyvyydet();
        self.nopeusVerlet= VelocityVerlet(LautaData.dt);
        self.seina = Seina();
        self.reiat = Reiat();
        self.keppi = Keppi();
        self.pallot = pallot;
        #self.piirtoalusta = PiirtoAlusta();
        #self.piirtoalusta.set_peli(self.biljardipeli)
        self.jatka = True;       
        self.pallotliikkuu = True;
        #self.piirtoalusta.piirra_keppi()

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

    def getPallot(self):
        return self.pallot
    
    def getPelaajat(self):
        return self.pelaajat
    
    def getKeppi(self):
        return self.keppi
    
    def getReiat(self):
        return self.reiat
    
    def getPallotLiikkuu(self):
        return self.pallotliikkuu
    
    def setPallotLiikkuu(self, pallotliikkuu):
        self.pallotliikkuu = pallotliikkuu
    
    def getJatka(self):
        return self.jatka

    def setPaivitettava(self, paivitettava):
        self.paivitettava = paivitettava
