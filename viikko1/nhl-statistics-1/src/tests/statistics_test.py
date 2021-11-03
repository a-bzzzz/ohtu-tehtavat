import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_loytaa_oikean_pelaajan(self):
        self.assertEqual(self.statistics.search("Kurri").name, ("Kurri"))
        self.assertEqual(self.statistics.search("Kurri").team, ("EDM"))
        self.assertEqual(self.statistics.search("Kurri").goals, (37))
        self.assertEqual(self.statistics.search("Kurri").assists, (53))
        self.assertEqual(self.statistics.search("Kurri").points, (90))

    def test_ei_loyda_vaaraa_pelaajaa(self):
        self.assertEqual(self.statistics.search("Selänne"), (None))

    
    def test_loytaa_joukkueen_pelaajat(self):
        self.assertEqual(str(self.statistics.team("DET")[0]), ("Yzerman DET 42 + 56 = 98"))
        self.assertEqual(str(self.statistics.team("EDM")[2]), ("Gretzky EDM 35 + 89 = 124"))

    def test_ei_loyda_vaaran_joukkueen_pelaajia(self):
        self.assertEqual(self.statistics.team("COL"), [])

    def test_loytaa_parhaan_pelaajan(self):
        self.assertEqual(str(self.statistics.top_scorers(1)[0]), ("Gretzky EDM 35 + 89 = 124"))
