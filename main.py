from player_character import PlayerCharacter

print("Welcome to The Valley of the Silver Wolf!")
name = input("What is your name? ") #Enter 'Soomin' as name
hometown = input("Which town of the Valley is your hometown? Blackstone, Fangmarsh, Leap-Creek, Pouch, or Underclaw? ")

name = PlayerCharacter(name, hometown)

print(name.STA)
print(name.POW)
print(name.AGI)
print(name.CHI)
print(name.WIT)
print(name.name)