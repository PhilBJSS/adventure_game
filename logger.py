import enum


from enum import Enum

class LogLevel(Enum):
    Dev = 0 
    Player = 1


class Logger:
    def __init__(self, level):
        self.level = level
    
    def log(self, msg, level):
        if level.value >= self.level.value:
            print(msg) 

    def logDev(self, msg):
        self.log(msg, LogLevel.Dev) 

    def logPlayer(self, msg):
        self.log(msg, LogLevel.Player) 
    