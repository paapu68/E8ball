# -*- coding: iso-8859-15 -*-
""" Biljardikeppiin liittyviä muuttujia ja funktioita """
from lautadata import LautaData

class Keppi:
    kulma=270.0 
    kulmaAskel=1.0
    poikkeama=0.01
    poikkeamaAskel=0.01

    
    def getKulmaRadian(self):
        from math import pi
        return self.kulma/360.0*2.0*pi

    def getVoima(self):
        """ voima jolla kepillä lyödään palloa (N) """
        return -LautaData.jousivakio*self.poikkeama

    def kierraVastapaivaan(self):
        """ lyontikeppiä kierretään vastapaivaan """
        self.kulma = self.kulma + self.kulmaAskel
        if (self.kulma > 360.0):
            self.kulma = self.kulma - 360.0;

    def kierraMyotapaivaan(self):
        """ lyontikeppiä kierretään myötäpaivaan """
        self.kulma = self.kulma - self.kulmaAskel
        if (self.kulma < 0.0):
            self.kulma = self.kulma + 360.0;
        
    def iske(self, pallo):
        """  Asetetaan pallolle kepin iskua vastaava lähtönopeus
        johon kepin isku kohdistuu
        f=m*a = m*dv/dt
        dv=f*dt/m """
        from math import cos, sin
        pallo.setPalloVX(-self.poikkeama_x*LautaData.jousivakio)
        pallo.setPalloVY(-self.poikkeama_y*LautaData.jousivakio)                
        #pallo.setPalloVX(-LautaData.dt/LautaData.pallonMassa*
        #                 self.getVoima()*self.poikkeama_x)
        #pallo.setPalloVY(-LautaData.dt/LautaData.pallonMassa*
        #                 self.getVoima()*self.poikkeama_y)
        print "VX, VY", pallo.getPalloVX(), pallo.getPalloVY()
        #sys.exit()
    
    def setPoikkeama(self,sx1, sy1, sx2, sy2):
        from math import sqrt
        self.poikkeama = sqrt((sx1-sx2)**2 + (sy1-sy2)**2)

    def setPoikkeama_x(self,sx1, sx2):
        self.poikkeama_x = sx2-sx1

    def setPoikkeama_y(self,sy1, sy2):
        self.poikkeama_y = sy2-sy1        
   
