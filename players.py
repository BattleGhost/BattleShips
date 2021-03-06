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
        self.ships = (self.ship41, self.ship31, self.ship32, self.ship21,
                      self.ship22, self.ship23, self.ship11, self.ship12, self.ship13, self.ship14)

    def random_placing(self, field):
        for ship in self.ships:
            if random.randint(0, 1) == 1:
                ship.rotate()
            sh = False
            while not sh:
                sh = field.place_ship(ship, random.randint(1, 10), random.randint(1, 10))


class Bot:
    @staticmethod
    def choose_name(a, b):
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

    @staticmethod
    def specify_coordinate(enemy_field):
        attempt = 1
        r = 3
        lenmax = 4
        len2 = 0
        len3 = 0
        len4 = 0
        for i in range(10):
            for j in range(10):
                if enemy_field.map[i][j] == 4:
                    if i + 1 < 10:
                        if enemy_field.map[i + 1][j] == 4:
                            if i + 2 < 10:
                                if enemy_field.map[i + 2][j] == 4:
                                    if i + 3 < 10:
                                        if enemy_field.map[i + 3][j] == 4:
                                            len4 = 1
                                        else:
                                            len3 = len3 + 1
                                    len3 = len3 + 1
                                else:
                                    len2 = len2 + 1
                            else:
                                len2 = len2 + 1
                    else:
                        if j + 1 < 10:
                            if enemy_field.map[i][j + 1] == 4:
                                if i + 2 < 10:
                                    if enemy_field.map[i][j + 2] == 4:
                                        if i + 3 < 10:
                                            if enemy_field.map[i][j + 3] == 4:
                                                len4 = 1
                                            else:
                                                len3 = len3 + 1
                                        len3 = len3 + 1
                                    else:
                                        len2 = len2 + 1
                                else:
                                    len2 = len2 + 1
                if len4 == 0:
                    lenmax = 4
                elif len3 == 0:
                    lenmax = 3
                elif len2 == 0:
                    lenmax = 2
                else:
                    lenmax = 1
        for i in range(10):
            for j in range(10):
                if enemy_field.map[i][j] == 3:
                    for k in range(1, lenmax):
                        if i + k < 10:
                            if enemy_field.map[i + k][j] == 5:
                                for n in range(1, lenmax - k):
                                    if i - n > 0:
                                        if enemy_field.map[i - k][j] == 5:
                                            break
                                        else:
                                            return i - n, j
                                break
                            elif enemy_field.map[i + k][j] == 0 or enemy_field.map[i + k][j] == 1:
                                return i + k, j
                            else:
                                continue
                        elif enemy_field.map[i - k][j] != 5:
                            return i - k, j
                        else:
                            break
                    for k in range(1, lenmax):
                        if j + k < 10:
                            if enemy_field.map[i][j + k] == 5:
                                for n in range(1, lenmax - k):
                                    if i - n > 0:
                                        if enemy_field.map[i][j - k] == 5:
                                            break
                                        else:
                                            return i, j - n
                                break
                            elif enemy_field.map[i][j + k] == 0 or enemy_field.map[i][j + k] == 1:
                                return i, j + k
                            else:
                                continue
                        elif enemy_field.map[i][j - k] != 5:
                            return i, j - k
                else:
                    while attempt < 10:
                        pix = random.randint(0, 9)
                        piy = random.randint(0, 9)
                        if enemy_field.map[pix][piy] == 1:
                            return pix, piy
                        elif enemy_field.map[pix][piy] == 0:
                            xmax = pix + r
                            ymax = piy + r
                            xmin = pix - r
                            ymin = piy - r
                            if pix + r > 9:
                                xmax = 9
                            if piy + r > 9:
                                ymax = 9
                            if pix - r < 0:
                                xmin = 0
                            if piy - r < 0:
                                ymin = 0

                            for k in range(xmin, xmax - 1):
                                for h in range(ymin, ymax - 1):
                                    if enemy_field.map[k][h] == 1:
                                        return (pix, piy)
                        elif enemy_field.map[pix][piy] == 5 or enemy_field.map[pix][piy] == 4:
                            attempt = attempt
                        else:
                            attempt = attempt + 1
                    for i in range(10):
                        for j in range(10):
                            if enemy_field.map[i][j] == 0:
                                return i, j


class NormalBot(GameParticipants, Bot):
    def __init__(self):
        super().__init__()
        self.name = "[Normal Bot] " + Bot.choose_name(19, 36)

    @staticmethod
    def specify_coordinate(enemy_field):
        attempt = 1
        r = 2
        while (attempt < 10):
            pix = random.randint(0, 9)
            piy = random.randint(0, 9)
            for i in range(10):
                for j in range(10):
                    if (enemy_field.map[i][j] == 3):
                        if (enemy_field.map[i + 1][j] == 5):
                            if (i == 0):
                                break
                            return (i - 1, j)
                        else:
                            if (enemy_field.map[i + 1][j] == 3):
                                if (enemy_field.map[i + 2][j] == 5):
                                    if (i == 0):
                                        break
                                    return (i - 1, j)
                                else:
                                    if (enemy_field.map[i + 2][j] == 3):
                                        if (enemy_field.map[i + 3][j] == 5):
                                            if (i == 0):
                                                break
                                            return (i - 1, j)
                                        else:
                                            return (i + 3, j)
                                    else:
                                        return (i + 2, j)
                        if (enemy_field.map[i][j + 1] == 3):
                            if (enemy_field.map[i][j + 1] == 5):
                                if (j == 0):
                                    break
                                return (i, j - 1)
                            else:
                                if (enemy_field.map[i][j + 1] == 3):
                                    if (enemy_field.map[i][j + 2] == 5):
                                        if (j == 0):
                                            break
                                        return (i, j - 1)
                                    else:
                                        if (enemy_field.map[i][j + 2] == 3):
                                            if (enemy_field.map[i][j + 3] == 5):
                                                if (j == 0):
                                                    break
                                                return (i, j - 1)
                                            else:
                                                return (i, j + 3)
                                        else:
                                            return (i, j + 2)
            if (enemy_field.map[pix][piy] == 1):
                return (pix, piy)
            elif (enemy_field.map[pix][piy] == 0):
                xmax = pix + r
                ymax = piy + r
                xmin = pix - r
                ymin = piy - r
                if (pix + r > 9):
                    xmax = 9
                if (piy + r > 9):
                    ymax = 9
                if (pix - r < 0):
                    xmin = 0
                if (piy - r < 0):
                    ymin = 0

                for k in range(xmin, xmax - 1):
                    for h in range(ymin, ymax - 1):
                        if (enemy_field.map[k][h] == 1):
                            return (pix, piy)
            elif ((enemy_field.map[pix][piy] == 5) or (enemy_field.map[pix][piy] == 4)):
                attempt = attempt
            else:
                attempt = attempt + 1
        for i in range(10):
            for j in range(10):
                if (enemy_field.map[i][j] == 0):
                    return (i, j)


class HardBot(GameParticipants, Bot):
    def __init__(self):
        super().__init__()
        self.name = "[Hard Bot] " + Bot.choose_name(37, 54)

    @staticmethod
    def specify_coordinate(enemy_field):
        attempt = 1
        r = 1
        while (attempt < 15):
            pix = random.randint(0, 9)
            piy = random.randint(0, 9)
            for i in range(10):
                for j in range(10):
                    if (enemy_field.map[i][j] == 3):
                        if (enemy_field.map[i + 1][j] == 5):
                            if (i == 0):
                                break
                            return (i - 1, j)
                        else:
                            if (enemy_field.map[i + 1][j] == 3):
                                if (enemy_field.map[i + 2][j] == 5):
                                    if (i == 0):
                                        break
                                    return (i - 1, j)
                                else:
                                    if (enemy_field.map[i + 2][j] == 3):
                                        if (enemy_field.map[i + 3][j] == 5):
                                            if (i == 0):
                                                break
                                            return (i - 1, j)
                                        else:
                                            return (i + 3, j)
                                    else:
                                        return (i + 2, j)
                        if (enemy_field.map[i][j + 1] == 3):
                            if (enemy_field.map[i][j + 1] == 5):
                                if (j == 0):
                                    break
                                return (i, j - 1)
                            else:
                                if (enemy_field.map[i][j + 1] == 3):
                                    if (enemy_field.map[i][j + 2] == 5):
                                        if (j == 0):
                                            break
                                        return (i, j - 1)
                                    else:
                                        if (enemy_field.map[i][j + 2] == 3):
                                            if (enemy_field.map[i][j + 3] == 5):
                                                if (j == 0):
                                                    break
                                                return (i, j - 1)
                                            else:
                                                return (i, j + 3)
                                        else:
                                            return (i, j + 2)
            if (enemy_field.map[pix][piy] == 1):
                return (pix, piy)
            elif (enemy_field.map[pix][piy] == 0):
                if (pix == 0) and (piy == 0):
                    if ((enemy_field.map[pix][piy + 1] == 1) or (enemy_field.map[pix + 1][piy] == 1)):
                        return (pix, piy)
                elif (pix == 9) and (piy == 9):
                    if ((enemy_field.map[pix][piy - 1] == 1) or (enemy_field.map[pix - 1][piy] == 1)):
                        return (pix, piy)
                elif (pix == 0) and (piy == 9):
                    if ((enemy_field.map[pix][piy - 1] == 1) or (enemy_field.map[pix + 1][piy] == 1)):
                        return (pix, piy)
                elif (pix == 9) and (piy == 0):
                    if ((enemy_field.map[pix][piy + 1] == 1) or (enemy_field.map[pix - 1][piy] == 1)):
                        return (pix, piy)
                elif (pix == 0) and (piy == 9):
                    if ((enemy_field.map[pix][piy - 1] == 1) or (enemy_field.map[pix + 1][piy] == 1)):
                        return (pix, piy)
                elif (pix == 0):
                    if ((enemy_field.map[pix][piy - 1] == 1) or (enemy_field.map[pix + 1][piy] == 1) or (
                        enemy_field.map[pix + 1][piy] == 1)):
                        return (pix, piy)
                elif (piy == 0):
                    if ((enemy_field.map[pix - 1][piy] == 1) or (enemy_field.map[pix + 1][piy] == 1) or (
                        enemy_field.map[pix][piy + 1] == 1)):
                        return (pix, piy)
                elif (pix == 9):
                    if ((enemy_field.map[pix][piy - 1] == 1) or (enemy_field.map[pix][piy + 1] == 1) or (
                        enemy_field.map[pix - 1][piy] == 1)):
                        return (pix, piy)
                elif (piy == 9):
                    if ((enemy_field.map[pix - 1][piy] == 1) or (enemy_field.map[pix + 1][piy] == 1) or (
                        enemy_field.map[pix][piy - 1] == 1)):
                        return (pix, piy)
                elif ((enemy_field.map[pix][piy - 1] == 1) or (enemy_field.map[pix + 1][piy] == 1) or (
                    enemy_field.map[pix][piy + 1] == 1) or (enemy_field.map[pix - 1][piy] == 1)):
                    return (pix, piy)
                elif ((enemy_field.map[pix][piy] == 5) or (enemy_field.map[pix][piy] == 4)):
                    attempt = attempt
                else:
                    attempt = attempt + 1

        for i in range(10):
            for j in range(10):
                if (enemy_field.map[i][j] == 0):
                    return (i, j)


class Player(GameParticipants):
    def __init__(self, name="Player"):
        super().__init__()
        self.name = name

    @staticmethod
    def specify_coordinate():
        # Временный вариант выбора координат
        x = int(input("Введите Х:"))
        y = int(input("Введите Y:"))