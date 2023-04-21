import random
from player import Player
from building import Building
from items import Item

item_names = [
'spoon',
'flower vase',
'potato',
'letter opener',
'chocolate bar',
'pillow',
'bust of William Shakespeare',
'cheese',
'laptop',
'key',
'lead pipe',
'wine glass'
]

location_names = [
    'on the table',
    'inside the cupboard',
    'on the wall',
    'underneath the sofa',
    'beside the clock',
    'taped to the ceiling',
    'on the window sill',
    'by the cat',
]

class Game:
    def __init__(self):
        self.mansion = Building()
        self.player  = Player("Bob", (0,0), self.mansion)
        room_coordinates = list(self.mansion.rooms)
        for i in range(5):
            room_coordinate =  random.choice(room_coordinates)
            self.mansion.rooms[room_coordinate].add_item(random.choice(location_names), random.choice(item_names))

    def play(self):

        while (True):
            print(f"{self.mansion.whichRoom(self.player.position)}")  #kitchen
            hasFoundItems = self.player.look_around()
            if hasFoundItems: 
                itemToTake = input("Enter item to pick up: ")
                self.player.pick_up(itemToTake)
            self.player.check_inventory()
            if len(self.player.items)>0:
                itemToPlace = input("Enter item to put down: ")
                self.player.put_down(itemToPlace)
                self.player.check_inventory()
            if self.mansion.whichRoom(self.player.position) == 'west hallway':
                break
            movechar = input("Enter a direction: ")
            self.player.move(movechar)


if __name__ == "__main__":
    game = Game()
    game.play()



