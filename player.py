class Action:
     def __init__(self, description, func):
        self.description = description
        self.func = func

class Player:
    def __init__(self, name, position, building):
        self.name = name
        self.position = position
        self.building = building
        self.items = []
    
    def move(self, direction):
        movement = (0,0)
        match direction:
            case "w":
                movement = (-1, 0)
            case "a":
               movement = (0, -1)
            case "s":
                movement = (1, 0)
            case "d":
                movement = (0, 1)
            case _:
                print("That is not a valid direction")
        newRow = (self.position[0] + movement[0])
        newCol = (self.position[1] + movement[1])
        newPosition = (newRow, newCol)
        try:
            self.building.whichRoom(newPosition)
        except:
            print("bounced")
        else:
           self.position = newPosition 
        
    def look_around(self):
        items = self.building.itemsInRoom(self.position)
        haveFoundItems = len(items) > 0 
        return haveFoundItems

    def pick_up(self, itemName):
       room = self.building.where(self.position)
       item = room.take_item(itemName)
       if item != None:
           self.items.append(item)

    def put_down(self, itemName, inputLocation):
        location = 'on the floor'
        room = self.building.where(self.position)
        for place in room.items:
            if place == inputLocation:
                location = inputLocation
        if location != inputLocation:
            print(f'You cannot put the {itemName} {inputLocation}')
        for item in self.items: 
            if item.name == itemName and room.items[location] == None :
                print(f'you put the {itemName} {location}')
                room.place_item(item, location)
                self.items.remove(item)
                return
            elif item.name == itemName:
                print(f'There is no space {location}')
                return
        print(f'you do not have {itemName}')
            
    def check_inventory(self): 
        if len(self.items) == 0:
            print("you have no items")
            return
        for item in self.items:
            print(f'you have a {item.name}')

    def describe_location(self): 
        print(f"You are in the {self.building.whichRoom(self.position)}")

    def pick_action(self):
        print("What would you like to do?")
        options = [
            Action("Look around", self.look_around), 
            Action("Check inventory", self.check_inventory), 
            Action("Pick up item", self.pick_up), 
            Action("Put down item", self.put_down), 
            Action("Move", self.move)
            ]
        for i in range(len(options)):
            print(f"{i+1}) {options[i].description}")
        playerInput = input()
        playerInputInt = int(playerInput) - 1 
        action = options[playerInputInt]
        action.func()