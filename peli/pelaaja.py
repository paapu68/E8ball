# -*- coding: iso-8859-15 -*-
"""
 * Sis�lt�� pelaajaan liittyv�t tiedot: pisteet, mink� v�risi� palloja
 * yritt��, yritt��k� mustaa palloa, onko voittanut tai h�vinnyt.
"""
class Pelaaja:

    def __init__(self):
        self.pallojaJaljella = 7;
        self.yritanVaria = "enTieda";
        self.yritanMustaaPalloa = False;
        self.voittanut = False;
        self.havinnyt = False;

    def vahennaPallojaJaljella(self, lisays):
        self.pallojaJaljella = self.pallojaJaljella - lisays
    
    def getPallojaJaljella(self):
        return self.pallojaJaljella;
    
    def setYritanVaria(self, vari):
        if (vari == "punainen"):
            self.yritanVaria = vari;
        if (vari == "sininen"):
            self.yritanVaria = vari;
        if (vari == "musta"):
            self.yritanVaria = vari;

    def getYritanVaria(self):
        return self.yritanVaria

    def setYritanMustaaPalloa(self, yritanMustaa):
        self.yritanMustaaPalloa = yritanMustaa;
        self.setYritanVaria("musta");        
    
    def getYritanMustaaPalloa(self):
        return self.yritanMustaaPalloa;

    def setHavinnyt(self, havinnyt):
        self.havinnyt = havinnyt
    
    def getHavinnyt(self):
        return self.havinnyt;
    
    def setVoittanut(self, voittanut):
        self.voittanut = voittanut

    def getvoittanut(self):
        return self.voittanut
