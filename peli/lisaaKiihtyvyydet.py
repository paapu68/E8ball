# -*- coding: iso-8859-15 -*-
"""
* Pallojen keskinäisistä voimista aiheutuvat kiihtyvyydet
* lisätään palloihin. 
* kiihtyvyydet aiheutuvat:
* 1) pallojen keskinäisistä coulombin voimista
* (lisaaCoulombKiihtyvyydetBiljardiPallot)
* 2) pallojen välisestä hard-core repulsiosta, joka estää pallojen
* menemisen päällekkäin
* (xxx funktio)
* 3) kitkasta joka pysäyttää liikkeen
* (xxx funktio)  
"""
from pelilauta.lautadata import LautaData
class LisaaKiihtyvyydet:
    """
    * Lisätään pallojen kiihtyvyyksiin
    * pallojen keskinäisistä Coulombin
    * voimista aiheutuvat kiihtyvyydet
    * ax = coulombsConstant * q1 * q2 * dx / (r² * mass)
    * ay = coulombsConstant * q1 * q2 * dy / (r² * mass)
    * yksiköt coulombi, metri, kilogramma
    * @param pallot Pallot jotka vuorovaikuttavat keskenään.
    """

    def lisaaCoulombKiihtyvyydetBiljardiPallot(self, pallot):
        from math import sqrt
        coulombsConstant = 8.987551787368*1000000000;
        
        p1 = pallot.getPallotArray();
        for pallo1 in p1:
            for pallo2 in p1:
                dx = pallo1.getPalloX() - pallo2.getPalloX();
                dy = pallo1.getPalloY() - pallo2.getPalloY();
                d2 = sqrt(dx*dx + dy*dy);
                varaus1 = pallo1.getPalloVaraus()
                varaus2 = pallo2.getPalloVaraus()
                massa = LautaData.pallonMassa
                if (d2 > 0.01):
                    pallo1.lisaaPalloAX(coulombsConstant * 
                                        varaus1 * varaus2 * dx / (d2 * massa))
                    pallo1.lisaaPalloAY(coulombsConstant * 
                                        varaus1 * varaus2 * dy / (d2 * massa))

    def lisaaHardCoreKiihtyvyydet(self, pallot):
        """
        * Lisätään pallojen kiihtyvyyksiin
        * pallojen overlap vuorovaikutus.
        * Eli kun pallot meinaavat mennä päällekkäin sen estää
        * Lennard Jones repulsio
        * @see http://en.wikipedia.org/wiki/Lennard-Jones_potential
        * Tässä vain repulsiivine C12 termi.
        * @param pallot Pallot jotka vuorovaikuttavat keskenään.
        """
        from math import pow, sqrt
        epsilon = 1e-13;
        minDist = LautaData.pallonHalkaisija /2.0
        p1 = pallot.getPallotArray()
        for pallo1 in p1:
            for pallo2 in p1:
                dx = pallo1.getPalloX() - pallo2.getPalloX()
                dy = pallo1.getPalloY() - pallo2.getPalloY()
                d = sqrt(dx*dx + dy*dy) - minDist
                d10 = pow(d,10);
                massa = LautaData.pallonMassa
                if (pallo1 != pallo2):
                    pallo1.lisaaPalloAX((epsilon * dx) / (d10 * massa));
                    pallo1.lisaaPalloAY((epsilon * dy) / (d10 * massa));
       
    def lisaaKitka(self, pallot):
        """
        * Lisätään kitkasta aiheuta hidastuvuus palloille.
        * Kitkan suunta on nopeutta vastaan.
        * @param pallot 
        * @see http://en.wikipedia.org/wiki/Friction#Dry_friction
        """
        gravitaatioVakio = 9.81;
        
        p = pallot.getPallotArray();
        for pallo in p:
            vx = pallo.getPalloVX();
            vy = pallo.getPalloVY();
            massa = LautaData.pallonMassa
            kitkaVoima = LautaData.kitkaKerroin * massa * gravitaatioVakio;
            pallo.lisaaPalloAX(-self.getYksikkoVektoriX(vx, vy)\
                               *kitkaVoima/massa);            
            pallo.lisaaPalloAY(-self.getYksikkoVektoriY(vx, vy)\
                               *kitkaVoima/massa);

    def getYksikkoVektoriX(self, x, y):
        from math import sqrt
        d = sqrt(x*x + y*y);
        if (d < 0.1):
            return 0.0;
        else:
            return x/d;

    def getYksikkoVektoriY(self, x, y):
        from math import sqrt
        d = sqrt(x*x + y*y);
        if (d < 0.1):
            return 0.0;
        else:
            return y/d;

