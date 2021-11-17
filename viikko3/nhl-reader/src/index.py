from datetime import datetime
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    players = reader.get_players()
    stats = PlayerStats(reader)
    country = input("\nAnna pelaajan kansalaisuus (3 ISOA kirjainta): ")
    top_players = stats.top_scorers_by_nationality(players, country)

    print("\nPlayers from " + top_players[0].nationality + " " + str(datetime.now()) + "\n")
    for player in top_players:
        print(player)

if __name__ == "__main__":
    main()
