from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):

    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = Tekoaly()

        tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
