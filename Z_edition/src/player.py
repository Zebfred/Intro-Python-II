class Player():
    def __init__(me, name, current_room):
        me.name = name
        me.current_room = current_room


player1 = Player('George', 'treasure chamber')
print(player1.name)
print(player1.current_room)

#class User(Player)
class User():

    def __init__(me, name, userid, role)
        me.name = name
        me.userid = userid
        me.role = role

    @classmethod
    def from_input(cls):
        return cls(
            raw_input('Name:')),
            int(raw_input('User ID:')),
            int(raw_input('role: '))),
        )
    user = User.from_input()
