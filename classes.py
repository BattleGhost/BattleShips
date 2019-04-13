class Ship:
    def __init__(self, size, position):
        self.size = size
        self.position = position

    def rotate(self):
        if self.position == 1:
            self.position = 0
        else:
            self.position = 1

    def __repr__(self):
        return "Ship({},{})".format(self.size, self.position)

    def __str__(self):
        return "Ship {} blocks long with {} orientation".format(self.size, ("horizontal", "vertical")[self.position])


class Field:
    def __init__(self):
        self.map = [[0] * 10 for i in range(10)]
        self.__ships = list()

    def place_ship(self, ship, x, y):

        if ship.position == 0:
            if x + ship.size - 1 > 10 or x < 1:
                return False
            for i in range(ship.size):
                if self.map[y-1][x+i-1] != 0:
                    return False

            if y > 1 and y < 10 and x > 1 and x + ship.size - 1 < 10:
                for i in range(3):
                    self.map[y - 2 + i][x - 2] = 2
                    self.map[y - 2 + i][x + ship.size - 1] = 2
            elif y > 1 and y < 10 and x == 1:
                for i in range(3):
                    self.map[y - 2 + i][x + ship.size - 1] = 2
            elif y > 1 and y < 10 and x + ship.size - 1 == 10:
                for i in range(3):
                    self.map[y - 2 + i][x - 2] = 2
            elif y == 1 and x > 1 and x + ship.size - 1 < 10:
                for i in range(2):
                    self.map[y - 1 + i][x - 2] = 2
                    self.map[y - 1 + i][x + ship.size - 1] = 2
            elif y == 10 and x > 1 and x + ship.size - 1 < 10:
                for i in range(2):
                    self.map[y - 2 + i][x - 2] = 2
                    self.map[y - 2 + i][x + ship.size - 1] = 2
            elif y == 10 and x + ship.size - 1 == 10:
                for i in range(2):
                    self.map[y - 2 + i][x - 2] = 2
            elif y == 10 and x == 1:
                for i in range(2):
                    self.map[y - 2 + i][x + ship.size - 1] = 2
            elif y == 1 and x + ship.size - 1 == 10:
                for i in range(2):
                    self.map[y - 1 + i][x - 2] = 2
            elif y == 1 and x == 1:
                for i in range(2):
                    self.map[y - 1 + i][x + ship.size - 1] = 2
            for i in range(ship.size):
                if y > 1:
                    self.map[y - 2][x + i - 1] = 2
                if y < 10:
                    self.map[y][x + i - 1] = 2
                self.map[y-1][x+i-1] = 1

        else:
            if y + ship.size - 1 > 10 or y < 1:
                return False
            for i in range(ship.size):
                if self.map[y+i-1][x-1] != 0:
                    return False

            if y > 1 and y + ship.size - 1 < 10 and x > 1 and x < 10:
                for i in range(3):
                    self.map[y - 2][x - 2 + i] = 2
                    self.map[y + ship.size - 1][x - 2 + i] = 2
            elif x > 1 and x < 10 and y == 1:
                for i in range(3):
                    self.map[y + ship.size - 1][x - 2 + i] = 2
            elif x > 1 and x < 10 and y + ship.size - 1 == 10:
                for i in range(3):
                    self.map[y - 2][x - 2 + i] = 2
            elif x == 1 and y > 1 and y + ship.size - 1 < 10:
                for i in range(2):
                    self.map[y - 2][x - 1 + i] = 2
                    self.map[y + ship.size - 1][x - 1 + i] = 2
            elif x == 10 and y > 1 and y + ship.size - 1 < 10:
                for i in range(2):
                    self.map[y - 2][x - 2 + i] = 2
                    self.map[y + ship.size - 1][x - 2 + i] = 2
            elif x == 10 and y + ship.size - 1 == 10:
                for i in range(2):
                    self.map[y - 2][x - 2 + i] = 2
            elif x == 10 and y == 1:
                for i in range(2):
                    self.map[y + ship.size - 1][x - 2 + i] = 2
            elif x == 1 and y + ship.size - 1 == 10:
                for i in range(2):
                    self.map[y - 2][x - 1 + i] = 2
            elif x == 1 and y == 1:
                for i in range(2):
                    self.map[y + ship.size - 1][x - 1 + i] = 2
            for i in range(ship.size):
                if x > 1:
                    self.map[y + i - 1][x - 2] = 2
                if x < 10:
                    self.map[y + i - 1][x] = 2
                self.map[y+i-1][x-1] = 1
        self.__ships.append((ship, x, y))

    def del_ship(self, x, y):
        if self.map[y-1][x-1] == 1:
            for ship in self.__ships:
                isStop = False
                for i in range(ship[0].size):
                    if ship[0].position == 0:
                        if ship[1] + i == x and ship[2] == y:
                            isStop = True
                            break
                    else:
                        if ship[1] == x and ship[2] + i == y:
                            isStop = True
                            break
                if isStop == True:
                    self.__ships.remove(ship)
                    ships = self.__ships
                    self.__init__()
                    for sh in ships:
                        self.place_ship(sh[0], sh[1], sh[2])
                    break

        else:
            return False

    def __repr__(self):
        return self.map

    def __str__(self):
        self.__tempstr = ""
        for i in range(len(self.map)):
            if i > 0:
                self.__tempstr += "\n"
            for j in range(len(self.map[i])):
                self.__tempstr += str(self.map[i][j]) + " "
        return self.__tempstr

