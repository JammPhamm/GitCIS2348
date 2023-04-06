# Pham, James 10.15 zyLab
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    #get win percentage
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

