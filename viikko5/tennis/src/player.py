"""Player Class"""

class Player:
    """One of two players in Tennis Game"""
    def __init__(self, name):
        """Initalisation of one player"""
        self.name = name
        self.match_scores = 0

    def add_point(self):
        """Adds match scores for a player"""
        self.match_scores += 1
