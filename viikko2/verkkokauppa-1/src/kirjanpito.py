tapahtumat = []

class Kirjanpito:
    # __instanssi = None
    #
    # @staticmethod
    # def get_instance():
    #     if not Kirjanpito.__instanssi:
    #         Kirjanpito.__instanssi = Kirjanpito()
    #
    #     return Kirjanpito.__instanssi
  

    def __init__(self):
        self.tapahtumat = tapahtumat

    def lisaa_tapahtuma(self, tapahtuma):
        self.tapahtumat.append(tapahtuma)
        # print(self.tapahtumat[-1])

    # Mahdollisesti voisi käyttää erillistä metodia..
    # def hae_tapahtumat(self):
    #     # for tapahtuma in self.tapahtumat:
    #     #     print(tapahtuma)
    #     return self.tapahtumat

kirjanpito = Kirjanpito()
