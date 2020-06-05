# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes


room1 = Room('hallway', 'dark creepy')
print(room1.name)
print(room1.attributes)
print(room1)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
