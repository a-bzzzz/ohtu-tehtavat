"""Tennis Game"""
from player import Player

class TennisGame:
    """Tennis game scoring"""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def won_point(self, player):
        """Adds points"""
        player.add_point()

    def equal(self, m_score1):
        """Checks scores when equal points"""
        score = ""
        if m_score1 == 0:
            score = "Love-All"                                      
        elif m_score1 == 1:
            score = "Fifteen-All"
        elif m_score1 == 2:
            score = "Thirty-All"
        elif m_score1 == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        return score

    def over_forty(self, minus_result):
        """Checks scores when points over 40"""
        score = ""
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def points_to_score(self, temp_score):
        """Modifies points to game score"""
        score = ""
        if temp_score == 0:
            score = score + "Love"
        elif temp_score == 1:
            score = score + "Fifteen"
        elif temp_score == 2:
            score = score + "Thirty"
        elif temp_score == 3:
            score = score + "Forty"
        return score

    def under_or_forty(self, m_score1, m_score2):
        """Checks scores when points under 40"""
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = m_score1
            else:
                score = score + "-"
                temp_score = m_score2

            score = score + self.points_to_score(temp_score)
        return score

    def get_score(self):
        """Scores for players"""
        m_score1 = self.player1.match_scores
        m_score2 = self.player2.match_scores
        if m_score1 == m_score2:
            return self.equal(m_score1)
        elif m_score1 >= 4 or m_score2 >= 4:
            minus_result = m_score1 -  m_score2
            return self.over_forty(minus_result)
        else:
            return self.under_or_forty(m_score1, m_score2)
