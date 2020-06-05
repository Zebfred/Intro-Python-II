class Item():
    """The base class for all items"""
    def __init__(me, name, description, value):
        me.name = name
        me.location = description
        me.value = value

    def __str__(me):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


dagger = Item('dagger', 'treasure chamber', 5)
print(dagger.name)
print(dagger.location)
print(dagger.value)



class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
