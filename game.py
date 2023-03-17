class Player:
    def __init__(self, name, position, building):
        self.name = name
        self.position = position
        self.building = building
    
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
                pass #error handle invalid input
        newRow = (self.position[0] + movement[0])
        newCol = (self.position[1] + movement[1])
        newPosition = (newRow, newCol)
        try:
            self.building.whichRoom(newPosition)
        except:
            print("bounced")
        else:
           self.position = newPosition 
        


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

class Item:
    def __init__(self, name):
        self.name = name


mansion = Building()
player  = Player("Bob", (0,0), mansion)


print(f"{mansion.whichRoom(player.position)}")  #kitchen
player.move("s")
print(f"{mansion.whichRoom(player.position)}")  # w h
player.move("s")                                # bounced
print(f"{mansion.whichRoom(player.position)}")  # w h 
player.move("d")
print(f"{mansion.whichRoom(player.position)}")  # c h 
player.move("w")
print(f"{mansion.whichRoom(player.position)}")  # n h 
player.move("w")                                # bounced 
print(f"{mansion.whichRoom(player.position)}")  # n h

