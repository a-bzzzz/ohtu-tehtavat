from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostoskori = []
        self._hinta = 0

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        lkm = 0
        for ostos in self._ostoskori:
            tuotemaara = ostos.lukumaara()
            lkm += tuotemaara
        return lkm

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        korissa = False
        for ostos in self._ostoskori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                korissa = True
                ostos.muuta_lukumaaraa(1)
        if not korissa:
            self._ostoskori.append(Ostos(lisattava))
        tuotehinta = lisattava.hinta()
        self._hinta += tuotehinta
        return self._hinta

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        korissa = False
        for ostos in self._ostoskori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                korissa = True
                if ostos.lukumaara() > 1:
                    ostos.muuta_lukumaaraa(-1)
                elif ostos.lukumaara() == 1:
                    self._ostoskori.remove(ostos)
        if not korissa:
            return

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostoskori = []

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostoskori
