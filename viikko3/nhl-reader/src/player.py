class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.assists + self.goals
    
    def __str__(self):
        return (
            f"{self.name:20}"
            f"\t{self.team:5}"
            f"{(self.goals):2}"
            f" + {(self.assists):2}"
            f" = {(self.points):3}"
        )
