from player_character import PlayerCharacter


soomin = PlayerCharacter()

print(soomin.hp)
print(soomin.standing)
soomin.receive_damage(4)
print(soomin.hp)
print(soomin.standing)
soomin.receive_damage(1)
print(soomin.hp)
print(soomin.standing)
