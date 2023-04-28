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
        room = self.where(position)
        room.print_items()
        items = []
        for location in room.items:
            item = room.items[location]
            if item != None:
                items.append(item)
        return items

class Room:
    def __init__(self, name):
        self.name = name 
        self.items = {
            "on the floor": None
        }

    def add_item(self, location, name):
        self.items[location] = Item(name)

    def add_empty_location(self, location):
        self.items[location] = None

    def take_item(self, name): 
        for location in self.items: 
            item = self.items[location]
            if item == None:
                continue
            if item.name == name :
                print(f'you take the {name} from {location}')
                self.items[location] = None 
                return item
        print(f'you could not find the {name}')

    def place_item(self, item, location):
        self.items.update({location : item})

    def print_items(self):
        for location in self.items:
            item = self.items[location] 
            if item != None: 
                print(f'there is a {item.name} {location}')
            else: 
                print(f"there is nothing {location}")



# "on table" : Item("pan") #this is just an example