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
    
    def which_room(self, position):
        return self.where(position).name
    
    def print_items_in_room(self, position):
        room = self.where(position)
        room.print_items()
        items = []
        for location in room.items:
            item = room.items[location]
            if item != None:
                items.append(item)
        return items
    
    def items_in_room(self, position):
        room = self.where(position)
        return room.items

    def room_is_empty(self, position):
        room = self.where(position)
        return room.is_empty()

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

    def is_empty(self):
        for location in self.items:
            if self.items[location] != None:
                return False
        return True
