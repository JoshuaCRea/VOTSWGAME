import pytest
from player_character import PlayerCharacter
from game_manager import GameManager


cw_test_data = [
    ("Blackstone", "BSLC"),
    ("BSLC", "Leap-Creek"),
    ("Leap-Creek", "LCUC"),
    ("LCUC", "Underclaw"),
    ("Underclaw", "FMUC"),
    ("FMUC", "Fangmarsh"),
    ("Fangmarsh", "FMP"),
    ("FMP", "Pouch"),
    ("Pouch", "PBS"),
    ("PBS", "Blackstone"),
]
@pytest.mark.parametrize("start, expected", cw_test_data)
def test_move_player_CW(start, expected):
    pc = PlayerCharacter("Blackstone", GameManager())
    pc.location = start

    pc.move_player(1)

    assert pc.location == expected


def test_move_player_CCW():
    raise NotImplementedError