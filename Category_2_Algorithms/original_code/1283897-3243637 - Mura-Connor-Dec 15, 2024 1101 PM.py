#My name is Connor Mura - Welcome to my Python Game
import sys

#Introduces player to the game
print(r'You are a wasteland drifter who stumbled upon an open vault -vault 201- a place where ')
print(r'vault dwellers escaped the bombs during the great war. You grew up in a vault, though that')
print(r'was many years ago now. You wandered in to look for loot, hopefully a new fusion core for your')
print(r'power armor – as yours is getting quite low. You enter the vault and descend the staircase to')
print(r'the main level and exit your power armor in what appears to be a communal bunkhouse. Old tools')
print(r'clutter the shelves and floor. Must’ve been mechanics lodging. You take a walk around, noticing')
print(r'the power is still on, giving you hope for that fusion core when suddenly – BAM. As you fall')
print(r'you catch a glimpse of the man that hit you, a well-dressed man in a checker suit - then darkness.')
print(r'You awake in what appears to be the overseer’s office, near his desk you see a')
print(r'video feed for the rest of the vault. You see the bodies of raiders littering the floor near the stairway.')
print(r'It looks like some sort of conflict went down while you were out; between some raiders')
print(r'and great khans – another gang of raiders – and with them the man in the checkered jacket.')
print(r'They are calling him Benny, and he seems to be in charge. They are taking refuge in the doctor’s office,')
print(r'patching themselves up and stealing chems. They stripped you of your belongings – but the Khans')
print(r'who took them died in the fight. You know now what you must do.')
print(r'First you must collect your belongings, then you can take your revenge')
print(r'on Benny and the Khans and escape the vault. Your power armor is still')
print(r'in the communal bunkhouse, you wouldn’t dare fight without it – but you')
print(r'still need that fusion core. You can find those in the generator room.')
print(r'In the food storage area, you will find some stimpacks')
print(r'– in case things go sideways. In the cafeteria you will find your trusty revolver –')
print(r'always handy in a shootout. In the closet you will find your ammo.')
print(r'Also, in the guard station you will find the override key –')
print(r'it’s your ticket out of here and you don’t want to be caught in a losing fight')
print(r'with nowhere to run. You gather your composure and face the door to the hallway.')
print('-'*100)
#explains game to player
print('To move, enter "north", "east", "south", or "west".')
print('When asked to pick up item, respond "yes" or "no".')
print('Collect all six items before facing Benny or you are doomed')


# links rooms together
rooms = {

        'Overseer Office': {'west': 'Guard Station', 'item': 'none'},
        'Guard Station': {'north': 'Cafeteria', 'east': 'Overseer Office', 'south': 'Doctor Office', 'item': 'override key'},
        'Cafeteria': {'east': 'Generator Room', 'south': 'Guard Station', 'west': 'Closet', 'item': 'pistol'},
        'Generator Room': {'west': 'Cafeteria', 'item': 'fusion core'},
        'Closet': {'east': 'Cafeteria', 'south': 'Communal Bunkhouse', 'item': 'ammo'},
        'Communal Bunkhouse': {'north': 'Closet', 'east': 'Doctor Office', 'south': 'Food Storage', 'item': 'power armor'},
        'Food Storage': {'north': 'Communal Bunkhouse', 'item': 'Stimpack'},
        'Doctor Office': {'north': 'Guard Station', 'west': 'Communal Bunkhouse', 'item': 'none'},
        'Exit': {'item': 'none'}

    }

#allows the game to tell players which direction they can go
room_direction_options = {

    'Overseer Office': 'west',
    'Guard Station': 'north, east, or south',
    'Cafeteria': 'east, south, or west',
    'Generator Room': 'west',
    'Closet': 'east or south',
    'Communal Bunkhouse': 'north, east, or south',
    'Food Storage': 'north',
    'Doctor Office': 'none',
    'Exit': 'none'

}


#main function that runs the game
def main():
    global current_room
    global inventory
    while current_room != 'Doctor Office' or 'Exit':
        user_inventory_process()
        room_movement()
    while current_room == 'Doctor Office' or 'Exit':
       end_game_behavior()
       break

#loop that lets you travel the rooms
def room_movement():
    global current_room
    if current_room != 'Exit' or 'Doctor Office':
        user_command_options = room_direction_options[current_room]
        print('The direction(s) you can go are {}\n'.format(user_command_options))
        user_command_direction = input('Where would you like to go?')
        # validates the commands
        if user_command_direction not in rooms[current_room]:
            print('Response not recognized')
        if user_command_direction == 'exit':
            current_room = 'Exit'
            return current_room
        elif user_command_direction in rooms[current_room]:
            current_room = rooms[current_room][user_command_direction]
            return current_room
    if current_room == 'Exit' or 'Doctor Office':
        end_game_behavior()
        return


#allows player to see the items in the rooms and pick them up
def user_inventory_process():
    global current_room
    global inventory
    if current_room != 'Doctor Office' or 'Exit':
        print('-' * 100)
        print('-' * 100)
        print('You are in the', current_room)
        if rooms[current_room]['item'] not in inventory and rooms[current_room]['item'] != 'none':
            print('You find', rooms[current_room]['item'])
            user_command_add = input('Would you like to add to inventory? type "yes" or "no".')
            print('-' * 100)
            print('-' * 100)
            if user_command_add == 'no':
                print('Unwise')
                print('current inventory', inventory)
            elif user_command_add == 'yes' and rooms[current_room]['item'] != 'none':
                inventory.append(rooms[current_room]['item'])
                print('current inventory', inventory)
                return inventory
            else:
                print('Response not recognized')
        else:
            print('The room is empty')
        print('current inventory', inventory)
    if current_room == 'Exit' or 'Doctor Office':
        end_game_behavior()
        return


#ends the game
def end_game_behavior():
    global current_room
    global inventory
    if current_room == 'Doctor Office':
        print('-' * 100)
        print('-' * 100)
        print('You see Benny!')
        print('-' * 100)
        print('-' * 100)
        #checks the player's inventory to determine whether they win or lose
        if len(inventory) < 6:
            print('-' * 100)
            print('-' * 100)
            print('Benny:"Sorry kid - looks like you just had an 18k run of bad luck"')
            print('YOU GET SHOT AND KILLED')
            print('Game Over!')
            sys.exit()
        elif len(inventory) >= 6:
            print('-' * 100)
            print('-' * 100)
            print(
                'Benny:"Sorry kid, I know you collected all the items, but truth is - the game was rigged from the start"')
            print('YOU GET SHOT AND KILLED')
            print('You Win!!!')
            sys.exit()
    #exits the game
    if current_room == 'Exit':
        print('-' * 100)
        print('-' * 100)
        print(current_room)
        print('GoodBye!')
        sys.exit()

#sets starting room to the overseer office
current_room = 'Overseer Office'
inventory = []

main()
