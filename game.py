class Player:
    def __init__(self, name, position):
        self.name = name
        self.position_x = position[0]
        self.position_y = position[1]
    
    def move(self, direction):
        movement = (0,0)
        match direction:
            case "w":
                movement = (-1,0)
            case "a":
               movement = (0,-1)
            case "s":
                movement = (1,0)
            case "d":
                movement = (0,1)
            case _:
                pass #error handle invalid input
        self.position_x += movement[0]
        self.position_y += movement[1]


class Building:
    def __init__(self):
        self.rooms = {
        (0,0) : Room("kitchen"), (0,1) : Room("hallway"),
        (1,0) : Room("hallway"), (1,1) : Room("hallway"), (1,2) : Room("hallway"), (1,3) : Room("hallway"),
                                 (2,1) : Room("hallway"),
                                 (3,1) : Room("bedroom"),
        }


class Room:
    def __init__(self, name):
        self.name = name 
        self.items = {
            "on table" : Item("pan") #this is just an example
        }

class Item:
    def __init__(self, name):
        self.name = name


mansion = Building()

# print(mansion.rooms[(4,1)])

player  = Player("Bob", (0,0))

print(f"({player.position_x},{player.position_y})")

player.move("s")

print(f"({player.position_x},{player.position_y})")