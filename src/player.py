# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player(Item):
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def __str__(self):
        return f'Your name is {self.name}. The room is {self.currentRoom.name} and {self.currentRoom.description}'

    def moveRoom(self, direction):
        self.currentRoom = direction

    def takeItem(self, item):
        self.items.append(item)
        print()
        print(f'You picked up the item, it is {item.description}')

    def dropItem(self, Item):
        self.items.remove(Item)
        print(f'Goodbye {item.name}')
