class Team:

    def __init__(self, name, players, coach):
        self.name = name
        self.players = []
        self.coach = coach
        self.points = 0

    def add_player(self, name, players):
        self.players.append(name)

    def has_player(self, name, players):
        for player in players:
            if name == players[name]:
                return True
            else: return False

    def play_game(result):
        if result == True:
            self.points += 3


def team_has_name(name):
    return name

def team_has_players