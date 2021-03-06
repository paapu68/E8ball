# -*- coding: iso-8859-15 -*-
"""
 * biljardipallojen jono ja jonoon liittyvi� toimintoja.
 * Oletus: ensimm�isen� on ly�ntipallo ja toisena musta pallo. 
"""
from pallo import Pallo
from lautadata import LautaData
lautadata = LautaData();

class Pallot(Pallo):
    def __init__(self, **kwargs):
        self.pallot = []
        self.perusvaraus = 0.0
        self.asetaPallojenAlkupaikat()
        self.asetaPallojenVarit()

    def getPallotArray(self):
        return self.pallot

    def getLyontiPallo(self):
        """ Annetaan pallojonon ensimm�inen pallo 
            joka on valkoinen ly�ntipallo """
        return self.pallot[0]

    def getMustaPallo(self):
        """ Annetaan pallojonon toinen pallo joka on musta pallo """
        return self.pallot[1]

    def lisaaPallo(self, pallo):
        """ lis�� pallo pallojonoon """
        self.pallot.append(pallo)

    def poistaPallo(self, index):
        """ poista indexill� osoitettu pallo pallojonosta """
        dummy = self.pallot.pop(index)

    def nollaaNopeudet(self):
        """nollataan pallojonon pallojen x ja y nopeudet"""
        for pallo in self.pallot:
            pallo.setPalloVX(0.0)
            pallo.setPalloVY(0.0)

    def nollaaKiihtyvyydet(self):
        """nollataan pallojonon pallojen x ja y kiihtyvyydet"""
        for pallo in self.pallot:
            pallo.setPalloAX(0.0)
            pallo.setPalloAY(0.0)
            
    def suurinNopeus(self):
        """ haetaan pallojonon pallojen suurin nopeus """        
        from math import sqrt
        v = 0.0
        maxv = 0.0
        for pallo in self.pallot:
            v = sqrt(pallo.getPalloVX()*pallo.getPalloVX()
                     +pallo.getPalloVY()*pallo.getPalloVY());
            if (maxv < v):
                maxv = v
        return maxv

    def suurinKiihtyvyys(self):
        """ haetaan pallojonon pallojen suurin kiihtyvyys """        
        from math import sqrt
        a = 0.0
        maxa = 0.0
        for pallo in self.pallot:
            a = sqrt(pallo.getPalloAX()*pallo.getPalloAX()
                     +pallo.getPalloAY()*pallo.getPalloAY());
            if (maxa < a):
                maxa = a
        return maxa

    def arvoLyontiPallonPaikka(self, minX, minY, maxX, maxY, Dist):
        """
        * Arvotaan lyontipallolle uusi paikka
        * siten ett� se ei mene toisen pallon p��lle.
        """
        from random import random
        from math import sqrt
        lyontiPallo = self.pallot[0]
        minDist = 0.0;
        newx = 0.0;
        newy = 0.0;
        
        while (minDist < Dist):
            newx = minX + (random() * (maxX - minX));
            newy = minY + (random() * (maxY - minY));
            
            minDist = 100.0;      
            for pallo in self.pallot[1:]:
                d = sqrt((newx - pallo.getPalloX())
                         *(newx - pallo.getPalloX())+
                         (newy - pallo.getPalloY())
                         *(newy - pallo.getPalloY()));
                if (d < minDist):
                    minDist = d;
        lyontiPallo.setPalloX(newx);
        lyontiPallo.setPalloY(newy);

    def asetaPallojenAlkupaikat(self):
        """
        * Asetetaan pallojen alkupaikat.
        """
        from math import pi, sin
        from random import shuffle
        # valkoinen pallo ensin
        pallo = Pallo()
        pallo.setPalloX(lautadata.valkoinenX)
        pallo.setPalloY(lautadata.valkoinenY);
        self.pallot.append(pallo);
        # musta pallo toiseksi
        pallo = Pallo()
        pallo.setPalloX(lautadata.alkuX)
        pallo.setPalloY(lautadata.alkuY - 2.0*lautadata.pallonHalkaisija)
        self.pallot.append(pallo);
        # k�rkipallo
        pallo = Pallo()
        pallo.setPalloX(lautadata.alkuX)
        pallo.setPalloY(lautadata.alkuY);
        self.pallot.append(pallo); 
        
        xjono = []
        yjono = []
        y = lautadata.alkuY;
        for row in range(1,5):
            print sin(50.0/360.0*2.0*pi), pi
            x = lautadata.alkuX-(row+1)*sin(50.0/360.0*2.0*pi) *lautadata.pallonHalkaisija;
            y = y - lautadata.pallonHalkaisija;
            for column in range(0,row+1):
                x = x + lautadata.pallonHalkaisija*1.2;
                # ei laiteta mustaa palloa toiseen kertaan
                if (row == 2 and column ==1):
                    pass
                else:
                    print "row, column", row, column
                    xjono.append(x)
                    yjono.append(y)
                    #pallo = Pallo(x,y);
                    #self.pallot.append(pallo); 
        #arvotaan punaisten ja sinisten pallojen paikat
        indexes=range(0, 13)
        shuffle(indexes)
        #print "indexes", indexes, len(xjono), len(yjono)
        for index in indexes:
            pallo = Pallo()
            pallo.setPalloX(xjono[index])
            pallo.setPalloY(yjono[index])
            self.pallot.append(pallo); 
        
        #for pallo in self.pallot:
        #    print "pallo.x", pallo.x
        #exit()
            
    def asetaPallojenVarit(self):       
        """
        * Asetetaan pallojen varit.
        * vain 0. ja 1. pallo, muut v�ri varauksen perusteella
        """    
        # valkoinen pallo ensin
        self.pallot[0].setPalloVari("valkoinen");
        # musta pallo toiseksi
        self.pallot[1].setPalloVari("musta");
        # negatiiviset (punaiset pallot, 2-8)
        for i in range(2, 9):
            self.pallot[i].setPalloVari("punainen");
        # positiiviset (siniset pallot, 9-15)
        for i in range(9, 16):
            self.pallot[i].setPalloVari("sininen");

    def asetaPallojenPerusVaraus(self, varaus):
        """
        * Asetetaan pallojen perusvaraus (mikro coulumbeja)
        * punaiset saavat -perusvaraus ja siniset +perusvaraus
        * @param varaus perusvaraus mikrocoulombeissa
        """
        self.perusvaraus = varaus;
     
    def getPallojenPerusVaraus(self):
         return self.perusvaraus

    def asetaPallojenVaraukset(self):
        """
        * Asetetaan pallojen varaukset.
        * pallot 2-8 negatiivisia
        * pallot 9-15 positiivisia
        """
        # negatiiviset (punaiset pallot, 2-8)
        for i in range(2, 9):
            self.pallot[i].setPalloVaraus(-self.perusvaraus);
        # positiiviset (siniset pallot, 9-15)
        for i in range(9, 16):
            self.pallot[i].setPalloVaraus(self.perusvaraus);

