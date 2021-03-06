# -*- coding: iso-8859-15 -*-
"""
 * P�ivitet��n pallojen paikat ja nopeudet
 * kiihtyvyydet saadaan voimista (a=F/m)
 * Aika kuluu hyppayksin dt (sekunteina).
"""
class VelocityVerlet:

    def __init__(self, dt):
        self.dt = dt
        self.maxSiirtyma = -1.0

    def PaivitaVelocityVerlet(self, pallot):
        """
        * P�ivitet��n pallojen paikat ja nopeudet
        * velocity-verlet algoritmin avulla
        * @see http://en.wikipedia.org/wiki/Verlet_integration
        * @param pallot n�iden paikkoja ja nopeuksia muutetaan 
        """
        from math import sqrt
        from sys import exit
        coulombsConstant = 8.987551787368*1000000000;        
        self.maxSiirtyma = -1.0;
        p1 = pallot.getPallotArray()
        for pallo1 in p1:
            #print "YOLD,VYOLD", pallo1.getPalloY(), pallo1.getPalloVY() 
            axold = pallo1.getPalloAX();
            ayold = pallo1.getPalloAY();
            xold = pallo1.getPalloX();
            yold = pallo1.getPalloY();
            
            xnew = pallo1.getPalloX() + pallo1.getPalloVX() * self.dt\
                   + 0.5 * pallo1.getPalloAX() * self.dt * self.dt
            ynew = pallo1.getPalloY() + pallo1.getPalloVY()*self.dt\
                   + 0.5 * pallo1.getPalloAY() * self.dt * self.dt;
            pallo1.setPalloX(xnew)
            pallo1.setPalloY(ynew);
            vxnew = pallo1.getPalloVX() 
            + 0.5 * (axold + pallo1.getPalloAX()) * self.dt; 
            vynew = pallo1.getPalloVY() 
            + 0.5 * (ayold + pallo1.getPalloAY()) * self.dt;
            pallo1.setPalloVX(vxnew);
            pallo1.setPalloVY(vynew);
            siirtyma = sqrt((xold-xnew)*(xold-xnew) 
                    + (yold-ynew)*(yold-ynew));
            if (siirtyma > self.maxSiirtyma):
                self.maxSiirtyma = siirtyma;
            #print "YNEW,VYNEW", pallo1.getPalloY(), pallo1.getPalloVY()
        #exit()

    def getMaxSiirtyma(self):
        """
        * Palauttaa pallojen jonosta suurimman siirtym�n, 
        * eli kuinka paljon pallo on maksimissaan liikkunut aika-askelten
        * v�lill�.
        * @return suurin pallon liikkuma matka
        """
        return self.maxSiirtyma
    
    def setMaxSiirtyma(self, x):
        self.maxSiirtyma = x

