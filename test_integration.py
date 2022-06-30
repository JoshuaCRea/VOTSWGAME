from cmath import e
from game_manager import GameManager


def test_player_wins():
    gm = GameManager()

    player = gm.players[0]

    # Manually set RepRank to 5 to ensure that no cards are filtered (so as not to throw exception internally)
    player.rep_rank = 5

    drawn_cards = gm.draw_quest_cards(player)

    selected_card = gm.select_card(drawn_cards)

    # Manually set DC to 0 so that Player always wins
    selected_card.difficulty_class = 0
    selected_card.rewards["stat_bonus"] = "POW"

    player_stat_before_quest = player.abilities["POW"]
    gm.execute_quest(player, selected_card)

    expected_technique = selected_card.rewards["technique"]

    assert player.techniques[0] == expected_technique
    assert player.abilities["POW"] == player_stat_before_quest + 1
    assert len(gm.schools["Blackstone"].quest_cards) == 19

