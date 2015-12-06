# -*- coding: iso-8859-15 -*-
"""
 *  Sis�lt�� pallon 2d paikan, 2d nopeuden, 2d kiihtyvyyden
 *  massan varauksen ja v�rin
 *  sek� metodit niiden asettamiseen ja antamiseen ulos
 *  Ly�ntipallon v�ri on 'valkoinen' mustan pallon v�ri on 'musta'
 *  yksik�t m, , m/s, m/s�, kg, mikro Coulomb
 * 
"""
from pelilauta.lautadata import LautaData
from sys import exit
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, BooleanProperty
from kivy.graphics import Ellipse, Color, Rectangle

lautadata = LautaData()

class Pallo(Widget):
    ball_d = NumericProperty(lautadata.pallonHalkaisija)
    x = NumericProperty()
    y = NumericProperty()

    def __init__(self, **kwargs):
        """
        *  @param x pallon x koordinaatti
        *  @param y pallon y koordinaatti
        *  vx pallon x suunnan vauhti
        *  vy pallon y suunnan vauhti
        *  ax pallon x suunnan kiihtyvyys
        *  ay pallon y suunnan kiihtyvyys
        *  varaus pallon varaus mikrocoulombeina
        *  vari pallon v�ri
        """
        super(Pallo,self).__init__(**kwargs)
        self.ball_d = lautadata.pallonHalkaisija
        self.x = -1
        self.y = -1
        self.vx = 0.0;
        self.vy = 0.0;
        self.ax = 0.0;
        self.ay = 0.0;
        self.varaus = 0.0;
        self.vari = "";
            
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
        """ lis�t��n pallon kiihtyvyyden x komponenttia """
        self.ax = self.ax + ax

    def lisaaPalloAY(self, ay):
        """ lis�t��n pallon kiihtyvyyden y komponenttia """
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
