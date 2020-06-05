class Player():
    def __init__(me, name, current_room):
        me.name = name
        me.current_room = current_room


player1 = Player('George', 'treasure chamber')
print(player1.name)
print(player1.current_room)
