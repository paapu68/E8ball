# -*- coding: iso-8859-15 -*-
"""
 * Biljardip�yd�n reikien koordinaatit kahdessa ArrayList:ss�
 * Toisessa x koordinaatit toisessa y.
 * Lis�ksi metodeja joissa tutkitaan onko pallo mennyt reik��n.
"""
class Reiat:
    """
    * Alustetaan 6 reik�� paikoilleen
    * @param reiatX reikien x koordinaatit reaaliavaruudessa
    * @param reiatY reikien y koordinaatit reaaliavaruudessa
    * 'mitaReiissa' kertoo montako palloa kutakin v�ri�
    * on mennyt reikiin t�m�n ly�nnin aikana.
    """

    def __init__(self):
        from lautadata import LautaData        
        self.reiatX = []
        self.reiatX.append(LautaData.minLautaX)
        self.reiatX.append(LautaData.minLautaX)
        self.reiatX.append(LautaData.minLautaX)
        self.reiatX.append(LautaData.maxLautaX-LautaData.pallonHalkaisija)
        self.reiatX.append(LautaData.maxLautaX-LautaData.pallonHalkaisija)
        self.reiatX.append(LautaData.maxLautaX-LautaData.pallonHalkaisija)
        self.reiatY = []
        self.reiatY.append(LautaData.minLautaY)
        self.reiatY.append(LautaData.maxLautaY*0.5)
        self.reiatY.append(LautaData.maxLautaY)
        self.reiatY.append(LautaData.minLautaY)
        self.reiatY.append(LautaData.maxLautaY*0.5)
        self.reiatY.append(LautaData.maxLautaY)                
        
        #LautaData lautadata = new LautaData();
        self.mitaReiissa = {}
        self.mitaReiissa["musta"] = 0
        self.mitaReiissa["valkoinen"] = 0
        self.mitaReiissa["punainen"] = 0
        self.mitaReiissa["sininen"] = 0
        self.ekanaReiassa = "enTieda"
        jotainReiissa = False

    def resetoiReiat(self):
        self.mitaReiissa["musta"] = 0
        self.mitaReiissa["valkoinen"] = 0
        self.mitaReiissa["punainen"] = 0
        self.mitaReiissa["sininen"] = 0
        self.ekanaReiassa = "enTieda"
    
    def setReikaXY(self, x, y):
        self.reiatX.append(x);
        self.reiatY.append(y);
    
    def getReiatX(self):
        return self.reiatX

    def getReiatY(self):
        return self.reiatY

    def lisaaReikiinMenneet(self, pallot):
        """ 
        * p�ivitet��n reikien sis�lt� jos palloja on mennyt reikiin.
        """

        for p1 in pallot.getPallotArray():
             if (not self.tarkastaPallo(p1)):
                 # pallo on reiassa            
                 vari = p1.getPalloVari();
                 lkm = self.mitaReiissa.get(vari);
                 lkm = lkm + 1;
                 self.mitaReiissa[vari] = lkm
        #for key, value in self.mitaReiissa.iteritems():
        #    print "vari, lkm", key, value
        
    def getMitaReiissa(self):
        """
        * otetaan t�m�nhetkinen tilanne mit� rei'iss� on.
        * @return dictionary joka kertoo montako mink�kin v�rist� 
        * palloa rei'iss� t�m�n ly�nnin aikana.
        """
        return self.mitaReiissa;
    
    def setEkanaReiassa(self, pallot):
        """ Mink� v�rinen pallo meni ensimm�isen� reik��n?
        * Vastaus on "enTieda" jos mit��n ei mennyt reik��n.
        """
        if (self.ekanaReiassa == "enTieda"):
            for p1 in pallot.getPallotArray():
                if (not(self.tarkastaPallo(p1))):
                    # pallo on reiassa
                    self.ekanaReiassa = p1.getPalloVari() 

    def getEkanaReiassa(self):
        return self.ekanaReiassa


    def tapaNormiPallot(self, pallot):
        """
        * Jos normipallo (eli ei valkoinen ly�ntipallo, eik� musta)
        * on mennyt reik��n niin se tapetaan pois
        * @param pallot biljardipallot 
        """
        p1 = pallot.getPallotArray()
        tapa = []
        for i in range(len(p1)-1, 1, -1):
            if (not(self.tarkastaPallo(p1[i]))):
                tapa.append(i)
        for t1 in tapa:
            pallot.poistaPallo(t1)
    
    def tarkastaPallo(self, pallo):
        """
        * Tutkitaan onko pallo mennyt reik��n.
        * @param pallo turkittava pallo
        * @return jos pallo on rei�ss� palautetaan false, muuten true
        """
        from math import sqrt
        from lautadata import LautaData
        
        jatka = True

        #print "tarkastaPallo(self, pallo):",len(self.reiatX)
        x = pallo.getPalloX()
        y = pallo.getPalloY()
        for j in range(0, len(self.reiatX)):
            d = sqrt((x-self.reiatX[j])**2
                +(y-self.reiatY[j])**2)
            #print "d", d
            if (d < LautaData.reianHalkaisija/2.0):
                jatka = False
        return jatka


