from items import Item

class Building:
    def __init__(self):
        self.rooms = {
        (0,0) : Room("kitchen"),      (0,1) : Room("north hallway"),
        (1,0) : Room("west hallway"), (1,1) : Room("central hallway"), (1,2) : Room("semi-east hallway"), (1, 3) : Room("east hallway"),
                                      (2,1) : Room("south hallway"),
                                      (3,1) : Room("bedroom"),
        }

    def whichRoom(self, position):
        return self.rooms[position].name


class Room:
    def __init__(self, name):
        self.name = name 
        self.items = {
            "on table" : Item("pan") #this is just an example
        }