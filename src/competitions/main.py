def add_one(number):
    return number + 1

class Match(object):
    
    def __init__(self, home_team, away_team, result=None) -> None:
        
        self.home_team = Team(home_team)
        self.away_team = Team(away_team)
        self.result = result
        
        self.ot = False
        self.finished = False
        if self.result is not None:
            self.finished = True
            if len(self.result) == 3:
                self.ot = True
    
class Team(object):
    
    def __init__(self, team_name) -> None:
        pass