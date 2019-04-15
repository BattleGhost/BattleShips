from players import *

field1 = Field()

ship21 = Ship(2, 1)
ship41 = Ship(4, 0)
ship11 = Ship(1, 0)
ship22 = Ship(2, 1)
field1.place_ship(ship21, 5, 5)
field1.place_ship(ship41, 7, 7)
field1.place_ship(ship11, 1, 2)
field1.place_ship(ship21, 9, 9)

print(field1, "\n")

field1.del_ship(8, 7)
print(field1)

field2 = Field()

bot1 = EasyBot()
bot2 = NormalBot()
bot3 = HardBot()
print(field2, "\n")
bot1.random_placing(field2)
print(field2, "\n")
print(bot1.specify_coordinate(field2))
print(bot2.specify_coordinate(field2))
print(bot3.specify_coordinate(field2))
