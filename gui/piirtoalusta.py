# -*- coding: iso-8859-15 -*-
"""
 * Piirretään pallot, reiät ja mahdollisesti lyöntikeppi.
 * xxx ei tehty pelitilanne
"""
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
#from peli.biljardipeli import Biljardipeli
from kivy.properties import ObjectProperty

class PiirtoAlusta(Widget):
    alusta = ObjectProperty(None)
    def __init__(self, **kwargs):
        #self.biljardipeli = biljardipeli
        self.biljardipeli = None
        self.keppi_points = []


        super(PiirtoAlusta, self).__init__(**kwargs)
        #with self.canvas:
        #   Color(1, 1, 0)
        #   d = 30.
        #   Ellipse(pos=(0, 0), size=(d, d))

    def set_peli(self, biljardipeli):
        self.biljardipeli = biljardipeli


    #def piirra_keppi(self):
    #    with self.canvas:
    #        self.keppi_points.append(0.1*self.width)
    #        self.keppi_points.append(0.1*self.height)
    #        self.keppi_points.append(1.0*self.width)
    #        self.keppi_points.append(1.0*self.height)
    #    print self.keppi_points


    def update(self):
        print "update!!!"
        #self.piirra_keppi()

    #def piirra_musta_pallo(self):
        

    def piirraReiat(self):        
        """
        * Piirretään reiat pelilaudalle
        * @param g grafiikka 
        """
        reiatX = self.biljardipeli.getReiat().getReiatX();
        reiatY = self.biljardipeli.getReiat().getReiatY();
        for i in range(0, len(reiatX)):
            Ellipse(pos=(lautadata.lautaDouble2PixelX(reiatX[i])-
                         lautadata.getreianHalkaisijaPixel()/2,
                         lautadata.lautaDouble2PixelY(reiatY[i])-
                         lautadata.getreianHalkaisijaPixel()/2), 
                         size=(lautadata.getreianHalkaisijaPixel(),
                               lautadata.getreianHalkaisijaPixel())
                    )
