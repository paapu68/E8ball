# -*- coding: iso-8859-15 -*-
"""
 * Pelilaudan seinien rajat annetaan reaalimaailmassa.
 * Lis�ksi metodi kimmauttamaan pallo sein�st�
"""
from lautadata import LautaData
lautadata = LautaData();

class Seina:
    def __init__(self):
        self.alax = lautadata.minLautaX;
        self.alay = lautadata.minLautaY;
        self.ylax = lautadata.maxLautaX;
        self.ylay = lautadata.maxLautaY;

    def VaihdaLiikemaara(self, pallot):             
        """
        * Jos pallo on l�hell� sein�� sen 
        * nopeus vaihdetaan vastakkaiseksi.  
        * @param pallot tutkittavat pallot 
        """
        
        p1 = pallot.getPallotArray()
        for pallo1 in p1:
            if (pallo1.getPalloX() <= self.alax):
                pallo1.setPalloVX(abs(pallo1.getPalloVX()))
            if (pallo1.getPalloX() >= self.ylax):
                pallo1.setPalloVX(-abs(pallo1.getPalloVX()))
            if (pallo1.getPalloY() <= self.alay):
                pallo1.setPalloVY(abs(pallo1.getPalloVY()))
            if (pallo1.getPalloY() >= self.ylay):
                pallo1.setPalloVY(-abs(pallo1.getPalloVY()))
            
    def getYlax(self):
        return self.ylax

    def getYlay(self):
        return self.ylay

    def getAlax(self):
        return self.alax

    def getAlay(self):
        return self.alay
