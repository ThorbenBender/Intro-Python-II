from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Simon', room['outside']);

if (player1.currentRoom == 'n_to'):
    print('It is true')

# Write a loop that:
while True:
#
# * Prints the current room name
    print(player1.currentRoom.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player1.currentRoom.description)
# * Waits for user input and decides what to do.
    print("You have 4 options where you can head to! [Nord]: n, [East]: e, [South]: south, [West]: west")
    playerChoice = input('In which direction do you want to go: ')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    # try:
    #     if(playerChoice == '')
#
# If the user enters "q", quit the game.
    try:
        if (playerChoice == 'n'):
            try:
                player1.currentRoom.n_to
                player1.moveRoom(room[player1.currentRoom.n_to.name.lower()])
            except AttributeError: 
                    player1.currentRoom.n_to = None
                    print('This direction is invalid!')
        elif(playerChoice == 'e'):
            try:
                player1.currentRoom.e_to
                player1.moveRoom(room[player1.currentRoom.e_to.name.lower()])
            except AttributeError: 
                    player1.currentRoom.e_to = None
                    print('This direction is invalid!')
        elif(playerChoice == 's'):
            try:
                player1.currentRoom.s_to
                player1.moveRoom(room[player1.currentRoom.s_to.name.lower()])
            except AttributeError: 
                    player1.currentRoom.s_to = None
                    print('This direction is invalid!')
        elif(playerChoice == 'w'):
            try:
                player1.currentRoom.w_to
                player1.moveRoom(room[player1.currentRoom.w_to.name.lower()])
            except AttributeError: 
                    player1.currentRoom.w_to = None
                    print('This direction is invalid!')
        else:
            break
    except ValueError: 
        break