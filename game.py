from player import Player
from building import Building
from items import Item

def game_loop():

    while (True):
        print(f"{mansion.whichRoom(player.position)}")  #kitchen
        player.look_around()
        if mansion.whichRoom(player.position) == 'west hallway':
            break
        movechar = input("Enter a direction: ")
        player.move(movechar)

if __name__ == "__main__":
    mansion = Building()
    player  = Player("Bob", (0,0), mansion)
    mansion.rooms[(0,1)].add_item('on the table', 'flower vase')
    game_loop()



