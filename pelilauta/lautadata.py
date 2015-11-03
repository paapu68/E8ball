# -*- coding: iso-8859-15 -*-
""" Tähän luokkaan talletetaan pelilautaan liittyvät mitta yms tiedot.
    see 'http://en.wikipedia.org/wiki/Billiard_table' """

class LautaData():
    dt = 1e-3 #aika-askel
    maxSiirtyma = 0.01
    maxNopeus = 0.001
    kitkaKerroin = 100.0
    minLautaX = 0.0
    minLautaY = 0.0;
    maxLautaX = 1.0;
    maxLautaY = 0.9;
    pallonHalkaisija = 0.02;
    pallonMassa = 0.0016;
    kepinPituus = 4.0 * pallonHalkaisija;
    reianHalkaisija = pallonHalkaisija * 1.6;
    scale = 1.0;
    pixelOffsetX = 0;
    pixelOffsetY = 0; 
    ph = pallonHalkaisija * scale
    pallonHalkaisijaPixel = int(ph)
    rh = reianHalkaisija * scale;
    reianHalkaisijaPixel = int(rh)
    pituusX = (maxLautaX - minLautaX) * scale;
    pituusXpixel = int(pituusX)
    pituusY = (maxLautaY - minLautaY) * scale;
    pituusYpixel = int(pituusY)
    alkuX = maxLautaX / 2.0;
    alkuY = 0.25 * maxLautaY;
    valkoinenX = alkuX;
    valkoinenY = 0.75*maxLautaY

    def lautaDouble2PixelX(self, x):
        """   * siirrytään reaalimaailman koordinaateista 
        * piirrettävän pelilaudan koordinaatteihin
        * x reaalimaailman x koordinaatti
        * @return pelilaudan x pixeli koordinaatti """
        return round(self.pixelOffsetX + self.scale*(x-self.minLautaX))

    def lautaDouble2PixelY(self, y):
        """   * siirrytään reaalimaailman koordinaateista 
        * piirrettävän pelilaudan koordinaatteihin
        * y reaalimaailman y koordinaatti
        * @return pelilaudan y pixeli koordinaatti """
        return round(self.pixelOffsetY + self.scale*(y-self.minLautaY))
