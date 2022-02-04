from competitions.main import Match, Team

def test_match():
    m = Match("a", "b")
    assert m.home_team.name == "a"
    assert m.away_team.name == "b"
    assert not m.finished
    assert not m.ot

def test_match_ot():
    m = Match("a", "b", (3, 2), True)
    assert m.finished
    assert m.ot

def test_match_result():
    m = Match("a", "b", (3, 2), False)
    assert m.result == (3,2)