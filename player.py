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
        