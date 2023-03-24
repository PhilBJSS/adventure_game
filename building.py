from items import Item

class Building:
    def __init__(self):
        self.rooms = {
        (0,0) : Room("kitchen"),      (0,1) : Room("north hallway"),
        (1,0) : Room("west hallway"), (1,1) : Room("central hallway"), (1,2) : Room("semi-east hallway"), (1, 3) : Room("east hallway"),
                                      (2,1) : Room("south hallway"),
                                      (3,1) : Room("bedroom"),
        }

    def where(self, position):
        return self.rooms[position]
    
    def whichRoom(self, position):
        return self.where(position).name
    
    def itemsInRoom(self, position):
        return self.where(position).print_items()
        

class Room:
    def __init__(self, name):
        self.name = name 
        self.items = {
        }

    def add_item(self, location, name):
        self.items[location] = Item(name)

    def print_items(self):
        for item in self.items:
            print(f'there is a {self.items[item].name} {item}')



# "on table" : Item("pan") #this is just an example