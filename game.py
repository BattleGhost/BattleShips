from players import *

field1 = Field()

ship21 = Ship(2, 1)
ship41 = Ship(4, 0)
field1.place_ship(ship21, 5, 5)
field1.place_ship(ship41, 7, 7)


print(field1, "\n")

field1.del_ship(8, 7)
print(field1)

field2 = Field()

bot = GameParticipants()
print(field2, "\n")
bot.random_placing(field2)
print(field2)
