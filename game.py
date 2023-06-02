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
    'in the fridge',
]

class Game:
    def __init__(self):
        self.mansion = Building()
        self.player  = Player("Bob", (0,0), self.mansion)
        room_coordinates = list(self.mansion.rooms)
        emptyLocationChance = 0.2
        for i in range(len(room_coordinates)):
            
            if len(item_names) > 0:
                item_name = random.choice(item_names)
            else:
                break

            room_coordinate = random.choice(room_coordinates)

            if len(location_names) > 0:
                location_name = random.choice(location_names)
            else:
                break

            if random.random() < emptyLocationChance:
                self.mansion.rooms[room_coordinate].add_empty_location(location_name)
                print(f'generated an empty location {location_name} in the {self.mansion.rooms[room_coordinate].name}')
                location_names.remove(location_name)
                continue

            self.mansion.rooms[room_coordinate].add_item(location_name, item_name)
            item_names.remove(item_name)
            location_names.remove(location_name)
            room_coordinates.remove(room_coordinate)
            print(f'generated a {item_name} {location_name} in the {self.mansion.rooms[room_coordinate].name}')

    def play(self):
        while (True):
            self.player.describe_location()
            self.player.pick_action()
            if self.mansion.whichRoom(self.player.position) == 'west hallway':
                break
           


if __name__ == "__main__":
    game = Game()
    game.play()



