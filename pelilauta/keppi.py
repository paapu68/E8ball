# -*- coding: iso-8859-15 -*-
""" Biljardikeppiin liittyvi� muuttujia ja funktioita """
from lautadata import LautaData

class Keppi:
    kulma=270.0 
    kulmaAskel=1.0
    poikkeama=0.01
    poikkeamaAskel=0.01
    jousivakio=10000.0

    def getKulmaRadian(self):
        from math import pi
        return self.kulma/360.0*2.0*pi


    def getVoima(self):
        """ voima jolla kepill� ly�d��n palloa (N) """
        return -self.jousivakio*self.poikkeama

    def kierraVastapaivaan(self):
        """ lyontikeppi� kierret��n vastapaivaan """
        self.kulma = self.kulma + self.kulmaAskel
        if (self.kulma > 360.0):
            self.kulma = self.kulma - 360.0;

    def kierraMyotapaivaan(self):
        """ lyontikeppi� kierret��n my�t�paivaan """
        self.kulma = self.kulma - self.kulmaAskel
        if (self.kulma < 0.0):
            self.kulma = self.kulma + 360.0;
        
    def iske(self, pallo):
        """  Asetetaan pallolle kepin iskua vastaava l�ht�nopeus
        johon kepin isku kohdistuu
        f=m*a = m*dv/dt
        dv=f*dt/m """
        from math import cos, sin
        pallo.setPalloVX(-LautaData.dt/LautaData.pallonMassa*
                self.getVoima()*cos(self.getKulmaRadian()))
        pallo.setPalloVY(-LautaData.dt/LautaData.pallonMassa*
                self.getVoima()*sin(self.getKulmaRadian()))
    
    def setPoikkeama(self,sx1, sy1, sx2, sy2):
        from math import sqrt
        self.poikkeama = sqrt((sx1-sx2)**2 + (sy1-sy2)**2)
   
