# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self):
        return f'Your name is {self.name}. The room is {self.currentRoom.name} and {self.currentRoom.description}'

    def moveRoom(self, direction):
        self.currentRoom = direction