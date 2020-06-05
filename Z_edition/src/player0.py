# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, moves, attributes):
        self.name = name
        self.moves = moves
        self.attributes = attributes

    def room_placement(self):
        print("Hello I move " + self.moves)



player1 = Player('George','west', 'strong and tall')
print(player1.name)
print(player1.attributes)
print(player1.room_placement())

def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
    print(world.tile_exists(self.location_x, self.location_y).intro_text())

def move_north(self):
    self.move(dx=0, dy=-1)

def move_south(self):
    self.move(dx=0, dy=1)

def move_east(self):
    self.move(dx=1, dy=0)

def move_west(self):
    self.move(dx=-1, dy=0)
