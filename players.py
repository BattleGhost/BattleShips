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
        attempt = 1
        while (attempt<30) :
            pix = random.randint(0, 9)
            piy = random.randint(0, 9)
            for i in range(10):
                for j in range(10):
                    if (enemy_field.map[i][j]==3):
                        if (enemy_field.map[i + 1][j] == 5):
                            if(i==0):
                               break
                            return (i - 1, j)
                        else:
                            if(enemy_field.map[i+1][j]==3):
                                if (enemy_field.map[i + 2][j] == 5):
                                    if (i == 0):
                                        break
                                    return (i - 1, j)
                                else:
                                    if (enemy_field.map[i+2][j]==3):
                                        if (enemy_field.map[i+3][j]==5):
                                            if (i == 0):
                                                break
                                            return (i -1, j)
                                        else:
                                            return (i+3,j)
                                    else:
                                        return (i + 2, j)
                        if(enemy_field.map[i][j+1]==3):
                            if (enemy_field.map[i][j+1] == 5):
                                if (j == 0):
                                    break
                                return (i, j-1)
                            else:
                                if (enemy_field.map[i][j+1] == 3):
                                    if (enemy_field.map[i][j+2] == 5):
                                        if (j == 0):
                                            break
                                        return (i, j-1)
                                    else:
                                        if (enemy_field.map[i][j+2] == 3):
                                            if (enemy_field.map[i][j+3] == 5):
                                                if (j == 0):
                                                    break
                                                return (i, j-1)
                                            else:
                                                return (i, j+3)
                                        else:
                                            return (i , j+2)
            if (enemy_field.map[pix][piy]==1):
                return (pix, piy)
            elif(enemy_field.map[pix][piy]==0):
                if ((j == 0)or(j == 1)or(j == 2)or(i == 0)or(i == 1)or(i == 2)):
                    attempt = attempt + 1
                else:
                    i = pix-2
                    j = piy-2
                    for i in range(5):
                        for j in range(5):
                            if (enemy_field.map[pix][piy]==1):
                                return (pix, piy)
            else:
                attempt = attempt +1
        return(pix, piy)
        #hi

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
        x= input()