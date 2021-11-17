from operator import attrgetter

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = []

    def top_scorers_by_nationality(self, list, nationality):
        for player in list:
            if player.nationality == nationality:
	            self.players.append(player)
        self.players.sort(reverse=True, key=attrgetter('points'))
        return self.players