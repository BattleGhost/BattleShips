from classes import *
import random

class GameParticipants:
    def __init__(self):
        self.ship11 = Ship(1, 0)
        self.ship12 = Ship(1, 0)
        self.ship13 = Ship(1, 0)
        self.ship14 = Ship(1, 0)
        self.ship21 = Ship(2, 0)
        self.ship22 = Ship(2, 0)
        self.ship23 = Ship(2, 0)
        self.ship31 = Ship(3, 0)
        self.ship32 = Ship(3, 0)
        self.ship41 = Ship(4, 0)
    def random_placing(self):
        pass

class Bot:
    @classmethod
    def choose_name(cls, a, b):
        return ["Armstrong", "Bandit", "Beast", "Boomer", "Buzz",
            "Casper", "Caveman", "C-Block", "Centice", "Chipper",
            "Cougar", "Dude", "Foamer", "Fury", "Gerwin", "Goose",
            "Heater", "Hollywood", "Vladimir", "Hound", "Iceman",
            "Imp", "Jester", "JM", "Junker", "Khan", "Maverick",
            "Middy", "Merlin", "Mountain", "Myrtle", "Outlaw",
            "Poncho", "Rainmaker", "Raja", "Rex", "Roundhouse",
            "Sabretooth", "Saltie", "Samara", "Scout", "Shepard",
            "Slider", "Squall", "Sticks", "Stinger", "Storm",
            "Sundown", "Sultan", "Swabbie", "Tusk", "Tex",
            "Viper", "Wolfman", "Yuri"][random.randint(a, b)]

class EasyBot(GameParticipants, Bot):
    def __init__(self):
        super().__init__()
        self.name = "[Easy Bot] " + Bot.choose_name(0, 18)
    def specify_coordinate(self, enemy_field):
        pass

class NormalBot(GameParticipants, Bot):
    def __init__(self):
        super().__init__()
        self.name = "[Normal Bot] " + Bot.choose_name(19, 36)
    def specify_coordinate(self, enemy_field):
        pass


class HardBot(GameParticipants, Bot):
    def __init__(self):
        super().__init__()
        self.name = "[Hard Bot] " + Bot.choose_name(37, 54)
    def specify_coordinate(self, enemy_field):
        pass


class Player(GameParticipants):
    def __init__(self, name = "Player"):
        super().__init__()
        self.name = name
    def specify_coordinate(self):
        #Временный вариант выбора координат
        x = int(input("Введите Х:"))
        y = int(input("Введите Y:"))