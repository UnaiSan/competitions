import itertools as it

class Match(object):
    
    def __init__(self, home_team, away_team, result=None, ot=False) -> None:
        
        self.home_team = Team(home_team)
        self.away_team = Team(away_team)
        self.result = result
        
        self.ot = ot
        self.finished = False
        if self.result is not None:
            self.set_result(result, ot)

    def set_result(self, result, ot=False):
        self.result = result
        self.finished = True
        
        # TODO: goals and points in this match different than in the tournament
        # Goals
        self.home_team.goals_scored += result[0]
        self.home_team.goals_received += result[1]
        self.away_team.goals_scored += result[1]
        self.away_team.goals_received += result[0]
        
        winner = result[1] - result[0]
        # Points
        self.home_team


class Team(object):
    
    def __init__(self, team_name) -> None:
        self.name = team_name
        
        self.games_played = 0
        self.goals_scored = 0
        self.goals_received = 0
        self.points = 0
        
    
    def __repr__(self) -> str:
        return f"{type(self)} {self.name} at {hex(id(self))}"

class Tournament(object):

    def __init__(self, list_of_teams=None, rounds=2) -> None:

        self.teams = [Team(t) for t in list_of_teams]

        self.matches = [Match(a, b) for a, b in it.permutations(list_of_teams, 2)]
        pass