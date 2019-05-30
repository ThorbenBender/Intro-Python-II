from room import Room
from player import Player
from item import Item
import random

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

items = [
    [Item('Sword', 'Shiny sword'), Item('Dagger', 'Is nice for close combat!')],
    [Item('Staff', 'can summon magic beasts'), Item('Ak-47', 'shoot')],
    [Item('Deagle', 'Click Heads'), Item('Waffel', 'Mmmh, tasty')],
    [Item('Duck', 'Cute, but deadly'), Item('Stick', 'It\'s just a stick')],
    [Item('Chainsaw', 'It\'s a chainsaw. Wow!'),
        Item('Flamethrower', 'Not a flamethrower!!')]
]
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


room['outside'].items = items[random.randint(0, 4)]
room['foyer'].items = items[random.randint(0, 4)]
room['overlook'].items = items[random.randint(0, 4)]
room['narrow'].items = items[random.randint(0, 4)]
room['treasure'].items = items[random.randint(0, 4)]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Simon', room['outside'])


# Write a loop that:
while True:
    #
    # * Prints the current room name
    print()
    print(player1.currentRoom.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player1.currentRoom.description)
# * Waits for user input of the item
    print()
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    # try:
    #     if(playerChoice == '')
#
# If the user enters "q", quit the game.
    while True:
        print('These are the items that exist in this room')
        for item in player1.currentRoom.items:
            print('==>', item)

        print()
        itemChoice = input(
            "Type Take and the item name to pick up the weapon you want or type None to not pick a weapon: ")
        if (itemChoice.split(' ')[0] == 'Take'):
            itemInput = itemChoice.split(' ')[1]
            itemExist = False
            for item in player1.currentRoom.items:
                if (itemInput == item.name):
                    itemExist = True
                    player1.takeItem(item)
                    player1.currentRoom.removeItem(item)
            if (itemExist):
                break
            else:
                print('Item doesn\' exist')
        elif(itemChoice.split(' ')[0] == 'Drop'):
            if (len(player1.items) < 1):
                print('Sorry you can\'t drop anything. You have no item.')
            else:
                itemExist = False
                for item in player1.items:
                    if (item.name == itemChoice.split(' ')[1]):
                        itemExist = True
                        player1.dropItem(item)
                        player1.currentRoom.addItem(item)
                if (itemExist):
                    break
                else:
                    print('This item doesn\'t exist!')
        else:
            print('This is an invalid command. You can either use Take or Drop')

    print('These are the items you possess!!')
    print()
    for item in player1.items:
        print('==>', item)

    print()
    print(
        'You can go in four different directions type \[n] for North \[e] for East \[s] for South \ [w] for West')
    print()
    playerChoice = input("Where do you want to go: ")
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
