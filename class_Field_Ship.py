class Field:
    # 0 вода
    # 1 постріл
    # 2 корабель не видно
    # 3 корабель поранено

    def create(self):
        abcdefghij = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        respyblika = [" ", "р", "е", "с", "п", "у", "б", "л", "і", "к", "а"]
        numbers = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        map = [[0] * 10 for i in range(10)]
        ''' for i in range(11):
            for j in range(11):
                if i == 0:
                    map[0][j]=numbers[j]
                if j == 0:
                    map[i][0]=abcdefghij[i]'''
        return map

    def show(self,map):
        abcdefghij = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        print("   1  2  3  4  5  6  7  8  9  10")
        for i in range(10):
            print(abcdefghij[i], map[i])

        '''for r in map:
            print(r)'''

    def change(self, map,x,y,a):
        map[x][y] = a




#class Block:


class Ship:
    '''def check(self, map, x, y,):
        if map[x][y] != 0:
            print("Error")
            return 9
        else:
            a = Field()
            a.change(map, x, y)
            return 1'''

    def position(self, map,x0,y0,x1,y1):
        '''if (x0>0 and y0>0 and x1>0 and y1>0 and x0<11 and y0<11 and x1<11 and y1<11):
            print("Error")
            return 9 '''
        if (x0 == x1 or y0 == y1):
            if (x0 != x1):
                if (x0>x1):
                    z = x0 - x1+1
                else:
                    z = x1 - x0+1
                    __c = x0
                    x0 = x1
                    x1 = __c
                y = y1
                x = x0
                for i in range(z):
                    a = Field()
                    a.change(map, x-1, y-1, 2)
                    x = x + 1
            elif (y0 != y1):
                if (y0 > y1):
                    z = y0 - y1+1
                else:
                    z = y1 - y0+1
                    y1=y0
                x = x1
                y = y1
                for i in range(z):
                    a = Field()
                    a.change(map, x-1, y-1, 2)
                    y = y + 1
            else:
                a = Field()
                a.change(map, x1-1, y1-1, 2)
        return 1

person1 = Field()
map1=person1.create()
person2= Ship()
person2. position(map1,5,10,5,8)
person1.show(map1)