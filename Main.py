from Player import Player

# get players name
playerNr=input("number of players: ")
playerLs=[]
for i in range(int(playerNr)): 
    playername = input("input name: ")
    player = Player(playername)
    playerLs.append(player)

# play to find winer = first 7
winner = False
while winner == False:
    for player in playerLs:
        print(str(player.__str__()))
        result = player.TakeTurn()
        input("***********next - press Enter***********")
        if result == 7:
            winner=True
            break

print("Game Over")            