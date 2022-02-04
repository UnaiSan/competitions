def add_one(number):
    return number + 1

class Match(object):
    
    def __init__(self, home_team, away_team, result=None, ot=False) -> None:
        
        self.home_team = Team(home_team)
        self.away_team = Team(away_team)
        self.result = result
        
        self.ot = ot
        self.finished = False
        if self.result is not None:
            self.finished = True
    
class Team(object):
    
    def __init__(self, team_name) -> None:
        self.name = team_name
        
        self.games_played = 0
        self.goals_scored = 0
        self.goals_received = 0
        self.points = 0
        pass