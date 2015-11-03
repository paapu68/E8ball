# -*- coding: iso-8859-15 -*-
"""
 *
 * Pelaajien jono ja pelaajiin liittyv�t toiminnot.
"""
from pelaaja import Pelaaja

class Pelaajat:

    def __init__(self):
        self.vuoro = 0;
        self.pelaajat = []
        pelaaja1 = Pelaaja()
        self.pelaajat.append(pelaaja1);
        pelaaja2 = Pelaaja()
        self.pelaajat.append(pelaaja2);
    
    def vaihdaVuoro(self):
        if (self.vuoro == 0):
            self.vuoro = 1
        else:
            self.vuoro = 0

    def vaihdaVaraukset(self, pallot):
        """
        * jos yritet��n punaisia palloja saa ly�ntipallo 
        * negatiivisen varauksen
        * samoin kuin musta pallo
        * vastaavasti jos
        * yritet��n sinisi� palloja saa ly�ntipallo 
        * positiivisen varauksen
        * samoin kuin musta pallo
        * @param pallot 
        """

        varaus = pallot.getPallojenPerusVaraus()
        if (self.getPelaaja().getYritanVaria() == "punainen"):
            pallot.getPallotArray()[1].setPalloVaraus(-varaus);
        if (self.getPelaaja().getYritanVaria() == "sininen"):
          pallot.getPallotArray()[1].setPalloVaraus(varaus);

    def getVuoro(self):
        return self.vuoro
    
    def getPelaaja(self):
        return self.pelaajat[self.vuoro]
    
    def alkaakoYrittaaMustaa(self, reiat):
        """     * jos omat pallot loppu aloittaa yrittaa mustaa
        """

        vari = self.getPelaaja().getYritanVaria();
        # jos ollaan vasta alussa ei voida yritt�� mustaa
        if (vari =="enTieda"):
            return;
        pussissa = reiat.getMitaReiissa().get(vari);
        if ((self.getPelaaja().getPallojaJaljella() -
                reiat.getMitaReiissa().get(vari)) == 0):
            self.getPelaaja().setYritanMustaaPalloa(True)

    
    def tarkastaTilanne(self, reiat, pallot):
        """
        * Pallojen pysahdyttya tutkitaan mit� tapahtui
        * @param reiat kertovat mit� sis�lt�v�t
        * @return jatketaanko peli�
        """

        #mit��n ei mennyt reikiin, vaihdetaan vuoro, peli jatkuu
        if (reiat.getEkanaReiassa() == "enTieda"):
            self.vaihdaVuoro();
            self.vaihdaVaraukset(pallot);
            return True
        
        # jos mustapallo meni reik��n katsotaan kumpi voitti, peli ei jatku
        if (reiat.getMitaReiissa()['musta'] == 1):
            if (self.getPelaaja().getYritanMustaaPalloa()):
                self.getPelaaja().setVoittanut(True)
                self.vaihdaVuoro()
                self.getPelaaja().setHavinnyt(True);
                self.vaihdaVuoro();
            else:
                self.getPelaaja().setHavinnyt(True);
                self.vaihdaVuoro();
                self.getPelaaja().setVoittanut(True);
                self.vaihdaVuoro();
            return False
        
        # pelaajien v�rit asetaan 
        # ensimm�isen pussituksen mukaan. Peli jatkuu.
        if (self.getPelaaja().getYritanVaria() == "enTieda"):
            self.getPelaaja().setYritanVaria(reiat.getEkanaReiassa())
            # asetetaan toisen pelaajan tavoittelemien pallojen v�ri
            if (self.getPelaaja().getYritanVaria() == "sininen"):
                self.vaihdaVuoro()
                self.getPelaaja().setYritanVaria("punainen")
                self.vaihdaVuoro()
            elif (self.getPelaaja().getYritanVaria() == "punainen"):
                self.vaihdaVuoro()
                self.getPelaaja().setYritanVaria("sininen")
                self.vaihdaVuoro()
       ## jos valkoinen pallo reik��n niin vuoro vaihtuu. Peli jatkuu
        if (reiat.getMitaReiissa()['valkoinen'] == 1):
            self.vaihdaVuoro()
            self.vaihdaVaraukset(pallot)
        
        # p�ivitet��n pistetilanne
        
        return True

