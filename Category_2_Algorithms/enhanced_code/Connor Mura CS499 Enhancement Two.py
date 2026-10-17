# ------- FALLOUT --------
#-------- By Connor Mura--

import sys

# stores player records
player_leaderboard = [
    {"name": "JohnnyFive", "moves": 20},
    {"name": "CourierSix", "moves": 30},
    {"name": "FrankHorrigan", "moves": 40}
]

def leaderboard_sort(data):
    # O(n^2) Bubble Sort for leaderboard records ranked by moves (ascending)
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]["moves"] > data[j + 1]["moves"]:
                data[j], data[j + 1] = data[j + 1], data[j]#swaps records
    return data

def score_search(sorted_data, target_score):
    # O(log n) Binary Search for player data
    low = 0
    high = len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2
        current_value = sorted_data[mid]["moves"]
        if current_value == target_score:
            return mid
        elif current_value < target_score:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def leaderboard_matrix(player_name, final_score):
    # Inserts player score into leaderboard, executes sorting, and verifies via search
    player_leaderboard.append({"name": player_name, "moves": final_score})
    print(f"High Score Entered for '{player_name}'")

    # Sorts leaderboard
    sorted_leaderboard = leaderboard_sort(player_leaderboard)

    print("\n----HIGH SCORE LEADERBOARD----")
    for Rank, entry in enumerate(sorted_leaderboard, 1):
        print(f"Rank {Rank}: {entry['name']} - Score {entry['moves']}")

    # Searchs leaderboard
    search_index = score_search(sorted_leaderboard, final_score)

    if search_index != -1:
        print(f"Player score ranked at [{search_index + 1}]")
    else:
        print("Player data not found")



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

#loop that lets players travel the rooms
def room_movement():
    global current_room, move_count

    if current_room == 'Exit' or current_room == 'Doctor Office':
        return current_room

    print(f"You are in the {current_room}")
    print(f"The direction(s) you can go are: {room_direction_options[current_room]}")
    user_command_direction = input('Where would you like to go?').strip().lower()

    # Move validation and tracking
    if user_command_direction in rooms[current_room]:
        current_room = rooms[current_room][user_command_direction]
        move_count += 1
    elif user_command_direction == 'exit':
        current_room = 'Exit'
    else:
        print("\n[!] Move not recognized")

    return current_room 

#allows player to see the items in the rooms and pick them up
def user_inventory_process():
    global current_room, inventory

    if current_room == 'Doctor Office' or current_room == 'Exit':
        return

    room_item = rooms[current_room]['item']

    if room_item != 'none':
        if room_item not in inventory:
            print('\n-' * 100)
            print(f"You are in the {current_room}.")
            print('-' * 100)
            print(f"You find {room_item}")

            user_command_add = input(f"Would you like to add to inventory? Type 'yes' or 'no': ").strip().lower()
            if user_command_add == 'yes':
                inventory.append(room_item)
                print(f"You added the {room_item} to your inventory. \nCurrent inventory: {inventory}")
            elif user_command_add == 'no':
                print("\nWho needs that junk anyways...")
            else:
                print("\n[!] Response not recognized")
        else:
            print("\nThe Room is empty.")
    else: 
        print("\nThe Room is empty.")


#handles end game behavior and reporting
def end_game_behavior():
    global current_room, inventory, move_count, username
    
    if current_room == 'Doctor Office':
        print('-' * 100)
        print('-' * 100)
        print('\nYou see Benny!')
        print('-' * 100)
        print('-' * 100)
        #checks the player's inventory to determine whether they win or lose
        if len(inventory) < 6:
            print('-' * 100)
            print('-' * 100)
            print('\nBenny:"Sorry kid - looks like you just had an 18k run of bad luck"')
            print('YOU GET SHOT AND KILLED')
            print('Game Over!')
            sys.exit()
        elif len(inventory) >= 6:
            print('-' * 100)
            print('-' * 100)
            print('\nBenny:"Sorry kid, I know you collected all the items, but truth is - the game was rigged from the start"')
            print('YOU GET SHOT AND KILLED')
            print('You Win!!!')
            leaderboard_matrix(username, move_count)
            sys.exit()

    #exits the game
    if current_room == 'Exit':
        print('-' * 100)
        print('-' * 100)
        print(current_room)
        print('GoodBye!')
        sys.exit()
    
#main function that runs the game
def main():
    global current_room, inventory, move_count, username

    #sets starting conditions
    current_room = 'Overseer Office'
    inventory = []
    move_count = 0

    #Introduces player to the game
    print("------ FALLOUT VAULT ESCAPE --------")
    username = input("Enter your name: ").strip()
    if not username:
        username = "VaultDweller"
    
    print(r'\nYou are a wasteland drifter who stumbled upon an open vault -vault 201- a place where ')
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

    while current_room != 'Doctor Office' and current_room != 'Exit':
        room_movement()
        user_inventory_process()
        end_game_behavior()

#runs game
main()


