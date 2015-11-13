# -*- coding: iso-8859-15 -*-
"""
 *  Sisältää pallon 2d paikan, 2d nopeuden, 2d kiihtyvyyden
 *  massan varauksen ja värin
 *  sekä metodit niiden asettamiseen ja antamiseen ulos
 *  Lyöntipallon väri on 'valkoinen' mustan pallon väri on 'musta'
 *  yksiköt m, , m/s, m/s², kg, mikro Coulomb
 * 
"""
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from pelilauta.lautadata import LautaData
from kivy.graphics import Ellipse, Color, Rectangle
from sys import exit

lautadata = LautaData()

class Pallo(Widget):
    #ball_d = NumericProperty(lautadata.pallonHalkaisija)
    #x = NumericProperty()
    #y = NumericProperty()

    def __init__(self, x, y, **kwargs):
        """
        *  @param x pallon x koordinaatti
        *  @param y pallon y koordinaatti
        *  vx pallon x suunnan vauhti
        *  vy pallon y suunnan vauhti
        *  ax pallon x suunnan kiihtyvyys
        *  ay pallon y suunnan kiihtyvyys
        *  varaus pallon varaus mikrocoulombeina
        *  vari pallon väri
        """
        super(Pallo, self).__init__(**kwargs)
        self.x = x;
        self.y = y;
        self.vx = 0.0;
        self.vy = 0.0;
        self.ax = 0.0;
        self.ay = 0.0;
        self.varaus = 0.0;
        self.vari = "";
        print "PALLO: self.width, self.height",self.width, self.height
        exit()
        with self.canvas:
            Color(1, 0, 0, 1)  # set the colour to red
            self.ellipse = Ellipse(pos=(self.x*self.width, self.y*self.height),
                                  size=(lautadata.pallonHalkaisija*self.width,
                                        lautadata.pallonHalkaisija*self.width))
            #self.ellipse = Ellipse(pos=self.center,
            #                      size=(lautadata.pallonHalkaisija*self.width,
            #                            lautadata.pallonHalkaisija*self.width))
            #self.rect = Rectangle(pos=self.center,
            #                      size=(self.width/2.,
            #                            self.height/2.))
        self.bind(pos=self.update_ball,
                  size=self.update_ball)

    def update_ball(self,*args):
        self.ellipse.pos = (self.x*self.width, self.y*self.height)
        self.ellipse.size = (lautadata.pallonHalkaisija*self.width,
                             lautadata.pallonHalkaisija*self.width)
        print "UPDATE x"

    def getPalloX(self):
        return self.x
    
    def getPalloY(self):
        return self.y
    
    def getPalloVX(self):
        return self.vx
    
    def getPalloVY(self):
        return self.vy
    
    def getPalloAX(self):
        return self.ax
    
    def getPalloAY(self):
        return self.ay

    def setPalloX(self, x):
        self.x = x
    
    def setPalloY(self, y):
        self.y = y
    
    def setPalloVX(self, vx):
        self.vx = vx
    
    def setPalloVY(self, vy):
        self.vy = vy
    
    def setPalloAX(self, ax):
        self.ax = ax
    
    def setPalloAY(self, ay):
        self.ay = ay

    def lisaaPalloAX(self, ax):
        """ lisätään pallon kiihtyvyyden x komponenttia """
        self.ax = self.ax + ax

    def lisaaPalloAY(self, ay):
        """ lisätään pallon kiihtyvyyden y komponenttia """
        self.ay = self.ay + ay

    def getPalloVari(self):
        return self.vari

    def setPalloVari(self, vari):
        self.vari = vari

    def getPalloVaraus(self):
        """Pallon varaus Coulombeissa """
        return self.varaus

    def setPalloVaraus(self, varaus):
        """asetetaan pallon varaus mikrocoulombeissa """
        self.varaus = varaus * 0.000001
