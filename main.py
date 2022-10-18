"""
OUTLINE
# SET UP
## IMPORT LIBRARIES
## DEFINE FUNCTIONS
    slow_print
    typing
    intro
    generate_door_code
    play_again
    player_died
    game_credits
    show_message_list
    read_messages
    launch_spaceship
    choose_weapon
    player_attack
    opponent_attack
    check_for_bar
    eat_bar_for_HP
    get_num
    check_code_guess
    guess_door_code
    avoid_asteroid
    escape_cell
    check_inventory
    change_inventory
    show_inventory
    display_funds
    show_shop_inventory
    purchase_item
## SET UP DICTIONARIES

### ACTUAL GAME ###
# WELCOME
# GAME START
## WAKE UP AT HOME
## SHOP
## GET ON SPACESHIP
## SPACE TRAVEL & ASTEROID
### EMERGENCY LANDING
## ARRIVE ON UDRERIA
## ESCAPE CELL
## BREAK INTO MAIN ROOM
## FREE MARZ
## BATTLE HEXT
"""


# SET UP
## IMPORT LIBRARIES
from random import randint
from time import sleep
from sys import stdout
from colorama import init
init(autoreset=True)
from colorama import Fore

## DEFINE FUNCTIONS
def slow_print(text, time = 1):
    """Prints text with a delay beforehand

    Parameters:
    text (str): Text to print
    time (float): Length of delay before printing, in seconds (default is 1)
    """

    sleep(time)
    print(text)


def typing(text, time = .1, space = True):
    """Prints text one character at a time.

    Parameters:
    text (str): Text to print
    time (float): Seconds between printing each character (default is .1)
    space (bool): Whether there is (True) or is not (False) a space between each character (default is True)
    """

    if space == True:
        for char in text:
            stdout.write(f"{char} ")
            stdout.flush()
            sleep(time)
    elif space == False:
        for char in text:
            stdout.write(f"{char}")
            stdout.flush()
            sleep(time)


def intro():
    """Introduces the game and gets player's name

    Returns:
    player_name (str): Player's name
    """

    typing("💫 THE SPECTACULAR SPACE ADVENTURE 💫", space = False)
    print()
    print()
    while True:
        typing("What is your name?\n", space = False)
        player_name = input("> ")
        if player_name == "":
            print("INVALID ENTRY: Must provide name")
        else:
            typing(f"\nPLAYER: {player_name}", space = False)
            print()
            print()
            break
    while True:
        typing("Type START to start the game\n", space = False)
        start = input("> ").upper()
        if start == "START":
            break
        else:
            print("INVALID ENTRY: Must enter START")

    print()
    typing("LOADING...")
    print()
    typing("INITIALIZING BOOSTERS...")
    print()
    typing("GATHERING STAR DUST...")
    print()
    typing("CALCULATING LIGHTYEARS...")
    print()
    typing("...", .5)
    print()
    print()
    typing(f"WELCOME {(player_name).upper()}")
    print()
    typing("LOCATION: MINO, XENON GALAXY")
    print()
    typing("MISSION BEGIN")
    print()

    sleep(1)
    print()
    typing("...", .5)
    print()
    print()
    sleep(1)

    return player_name


def generate_door_code(length):
    """Creates a list of random numbers without duplicates to use as door code

    Parameters:
    length (int): Length of list

    Returns:
    door_code (list of int): List of randomly selected int
    """

    door_code = []
    while len(door_code) < length:
        num = randint(0, 9)
        if num not in door_code:
            door_code.append(num)
    return door_code


def play_again():
    """Asks if player wants to play the game again.

    Returns:
    playing (bool): Whether the player does (True) or does not (False) want to play the game again 
    """

    typing("Do you want to play again? [Y/N]\n", space=False)
    while True:
        play_again = input("> ").upper()
        print()
        if play_again == "Y":
            typing("REINITIALIZING...", .2)
            print()            
            playing = True      # Game will start over
            break
        elif play_again == "N":
            typing("END TRANSMISSION.", .2)
            print()
            playing = False     #Game will end
            break
        else:
            print("INVALID ENTRY: Must enter Y or N")
    
    return playing


def player_died(reason):
    """Informs the player they died and the reason for their death, then asks if they want to play again.

    Parameters:
    reason (str): Reason for player's death

    Returns:
    playing (bool): Whether the player does (True) or does not (False) want to play the game again 
    """
    
    typing("CRITICAL FAILURE\n", .2)
    slow_print(reason, .5)
    print()
    playing = play_again()
    return playing


def game_credits():
    """Display game credits"""
    typing("🖤 CREDITS 🖤")
    print()
    typing("📝 Design, programming, & writing by Hanâ\n", space=False)
    print()
    typing("💾 Testing & feedback:\n", space=False)
    typing("Crystal\n", space=False)
    typing("Lo\n", space=False)
    print()
    typing("📚 Special thanks:\n", space=False)
    typing("Maily\n", space=False)
    typing("Sabrina\n", space=False)
    print()
    typing("Thanks for playing :)\n", space=False)


def show_message_list(message1, message2, message3):
    """Prints messages on player's holo-device, including read/unread status"""
    unread = "🌕"
    read = "🌑"

    if message1 == "unread":
        message_status = unread
    elif message1 == "read":
        message_status = read
    slow_print(Fore.GREEN + f"    (1) {message_status} SECURITY TEAM: ! Important notice for all Mino residents !")    

    if message2 == "unread":
        message_status = unread
    elif message2 == "read":
        message_status = read
    slow_print(Fore.GREEN + f"    (2) {message_status} MARZ: Hey {player_name}! Fancy a trip from your planet to...")

    if message3 == "unread":
        message_status = unread
    elif message3 == "read":
        message_status = read
    slow_print(Fore.GREEN + f"    (3) {message_status} NEWS ALERT: Planetary council members respond to possible Isotropa reemergence")


def read_messages():
    """Prompts the player to read through each of the messages on their holo-device."""
    message1 = "unread"
    message2 = "unread"
    message3 = "unread"

    message_header = "     - - - MESSAGE - - -"
    message_footer = "    - - - - END - - - -"

    # FOR TESTING ONLY
    # message1 = "read"
    # message2 = "read"
    # message3 = "read"

    while message1 != "read" or message2 != "read" or message3 != "read":
        show_message_list(message1, message2, message3)
        print()
        slow_print("Which message do you want to read?")
        message_choice = input("> ")
        print()

        if message_choice == "1": # SECURITY TEAM message
            slow_print(Fore.GREEN + f"{message_header}\n    SECURITY TEAM: ! Important notice for all Mino residents ! \n    This is a reminder that per our monthly schedule, we have assigned everyone new spaceship launch codes. Regularly changing launch codes is an important part of our security protocol. \n    Your new personal launch code is {spaceship_code}.\n{message_footer}")
            print()
            slow_print("You sigh. You know security protocol is important, but sometimes you wish they would change the codes a little less often. You can hardly memorize the code by the time you get assigned a new one.\n")
            message1 = "read"
        elif message_choice == "2": # MARZ message
            slow_print(Fore.GREEN + f"{message_header}\n    MARZ: Hey {player_name}! Fancy a trip from your planet to mine? It's been too long and I've got a special surprise for you.\n{message_footer}")
            print()
            slow_print("You're happy to hear from Marz. You two have been friends for a long time, but you've both been too busy to visit one another lately. Though surprises aren't usually their thing...\n")
            message2 = "read"
        elif message_choice == "3": # NEWS ALERT message
            slow_print(Fore.GREEN + f"{message_header}\n    NEWS ALERT: There have been unconfirmed reports that the Isotropa faction may be re-emerging. Planetary council members have made statements indicating this is unlikely. We will continue reporting on this as the story develops.\n{message_footer}")
            print()
            slow_print("Ugh, not the Isotropa. They were an authoritarian faction that had tried to seize control of a few nearby planets. They had been defeated 20 years ago, but if they really are popping back up then that can only spell bad news. Hopefully the reports turn out to be wrong...\n")
            message3 = "read"
        else:
            print("You should really check all of your messages (enter 1, 2, or 3).\n")
        if message1 != "read" or message2 != "read" or message3 != "read":
            slow_print("You still have unread messages.\n")


def launch_spaceship(spaceship_code):
    """Prompts player to enter spaceship code
    
    Prompts player to enter code for spaceship and loops until player enters correct code. If player has 2 wrong guesses, gives the player a hint.

    Parameters:
    spaceship_code (int): 4 digit code
    """

    incorrect_guesses = 0

    while True:
        entered_code = (input("    Enter the 4 digit launch code: "))

        if entered_code.isdigit() == False or len(entered_code) != 4:
            print("    INVALID ENTRY: MUST ENTER 4 NUMBERS")
            print()

        else:
            entered_code = int(entered_code)
            if entered_code == spaceship_code:
                print(Fore.GREEN + "    🟢 CORRECT CODE 🟢")
                break

            print(Fore.RED + "    🔴 INCORRECT CODE 🔴")
            incorrect_guesses += 1
            print()

            if incorrect_guesses >= 2:
                print("Hm, didn't that message from the Security Team say something about launch codes?")
                print()


def choose_weapon():
    """Prompts player to choose a weapon and returns their selection
    
    Returns:
    weapon (str): The weapon the player chose
    """

    print("Which gun do you want to use?")
    print(Fore.CYAN + f"    (1) Supersonic Boltslinger: {weapons['Supersonic Boltslinger']['description']}")
    print(Fore.CYAN + f"    (2) Turbogun: {weapons['Turbogun']['description']}")

    while True:
        weapon_choice = input("> ")
        print()
        if weapon_choice == "1":
            weapon = "Supersonic Boltslinger"
            break
        elif weapon_choice == "2":
            weapon = "Turbogun"
            break
        else:
            print("INVALID ENTRY: Must choose from available weapons (enter 1 or 2)")
    slow_print(Fore.BLUE + f"    💥 {weapon} equipped")
    
    return weapon


def player_attack(weapon, opponent, opponent_HP):
    """Fires player's weapon at opponent with a random chance of hitting the opponent.

    Prompts player to fire weapon by pressing RETURN key. Player has a random chance of hitting the opponent. If successful hit, subtracts the damage amount from the opponent's HP. Prints whether shot hit the opponent and the opponent's HP.

    Parameters:
    weapon (str): Name of weapon player is using (must be a key in weapons dictionary  - determines chance and damage of attack)
    opponent (str): Name of opponent
    opponent_HP (int): Amount of health the opponent has

    Returns:
    opponent_HP (int): Amount of health the opponent has after attack
    """

    chance = weapons[weapon]['chance']
    damage = weapons[weapon]['damage']
    
    num = randint(1,chance)

    if num == 1:
        opponent_HP -= damage
        opponent_HP = max(0, opponent_HP)
        slow_print(Fore.RED +f"You hit {opponent} (-{damage} HP)", .3)
    else:
        slow_print(Fore.YELLOW + "You miss", .3)

    slow_print(Fore.BLUE + f"    {opponent.upper()} HEALTH: {opponent_HP}", .3)
    
    return opponent_HP


def opponent_attack(opponent, player_HP):
    """Fires opponent's weapon at player.

    Fires opponents weapon at player with a random chance of hitting the player. If successful hit, subtracts the damage amount from the player's HP. Prints whether shot hit the player and the player's HP.

    Parameters:
    opponent (str): Name of opponent (must be a key in enemies dictionary - determines chance and damage of attack)
    player_HP (int): Amount of health the player has

    Returns:
    player_HP (int): Amount of health the player has after attack
    """

    chance = enemies[opponent]['chance']
    damage = enemies[opponent]['damage']

    num = randint(1,chance)

    if num == 1:
        player_HP -= damage
        player_HP = max(0, player_HP)
        slow_print(Fore.RED + f"{opponent} hits you (-{damage} HP)", .3)
    else:
        slow_print(Fore.YELLOW + f"{opponent} misses you", .3)

    slow_print(Fore.BLUE + f"    YOUR HEALTH: {player_HP}", .3)
    
    return player_HP


def check_for_bar():
    """Checks if user has the Moon Food Meal Bar in their inventory, and if they do, provides them with instructions on how to use it.
    """
    if "Moon Food Meal Bar" in inventory:
        slow_print(f"As you move to aim your {weapon}, your feel something against your leg in one of your pockets. Your Moon Food Meal Bar!\n")
        slow_print("This will certainly come in handy now. Good thing you stopped by the shop on your way out!\n")
        slow_print("When it's your turn to fire your weapon, type 'MOON FOOD MEAL BAR' to eat the bar instead of taking a shot. Restores your health by 2 points.")


def eat_bar_for_HP(player_HP):
    """Player eats meal bar and restores their HP by 2
    
    Parameters:
    player_HP (int): player's HP at time of function call

    Returns:
    player_HP (int): Amount of health the player has after eating the bar
    """

    slow_print(Fore.YELLOW + "You eat the Moon Food Meal Bar (+2 HP)", .3)
    player_HP += 2
    sleep(1)
    change_inventory("Moon Food Meal Bar", 1, "remove")
    slow_print(Fore.BLUE + f"    YOUR HEALTH: {player_HP}", .3)
    
    return player_HP


def get_num(num_len):
    """Get number from user, check criteria, and convert to int

    Asks the user for a number and checks whether the input is a number and is only a specified number of digits long. If it meets this criteria, it converts the input into an int. If it doesn't meet the criteria, it gives the user an error message and prompts them again. Repeats until criteria are met.

    Parameters:
    num_len (int): The length the user's number should be
  
    Returns:
    num_entry (int): The number the user guessed
    """
    
    num_entry = ""
    while True:
        num_entry = input("> ")
        if num_entry.isdigit() == False:
            print("ERROR: Must enter a number")
        elif len(num_entry) != num_len:
            if num_len == 1:
                print("ERROR: Must enter one digit")
            else:
                print(f"ERROR: Number must be {num_len} digits long")
        else:
            break
    num_entry = int(num_entry)
    return num_entry


def check_code_guess(guess, code, code_index):
    """Checks whether a user's guessed number is in a passcode.
  
    First it checks if the user's number is at the correct index. If not, it checks if the number is elsewhere in the code. It then returns a value that states whether the number is correct and if so, whether it is at the correct index.
  
    Parameters:
    guess (int): The user's guessed number
    code (list of int): The code to check the user's guess against
    code_index (int): The index location in the code (at which the guess is checked against)
  
    Returns:
    guess_value (str): Description of whether the guessed number is the correct number at the correct index, a correct number at the wrong index, or a wrong number entirely
    """

    if guess == code[code_index]:
        guess_value = Fore.GREEN + "correct number, correct location"
    else:
        if guess in code:
            guess_value = Fore.YELLOW + "correct number, wrong location"
        else:
            guess_value = Fore.RED + "wrong number"
    return guess_value


def guess_door_code():
    """
    The player is prompted to guess the 3 digit door code. They enter the digits one at a time (through the get_num(1) function, which checks that the player's input is a single numerical digit.) Each time the player enters a number, it "appears" on the display (this is what the print statements with the underscores are). The check_code_guess() function checks whether the numbers are correct and the results are stored in the variables guess1_value, guess2_value, and guess3_value. They then get told whether each of the numbers is the correct number in the correct location, a correct number but in the wrong location (i.e. it appears in a different part of the code), or a wrong number (i.e. it doesn't show up anywhere in the code). If the code they guessed is incorrect, they loop repeats itself. If it's correct, the loop ends.
    """
    guessed_code = []
    guess1 = ""
    guess2 = ""
    guess3 = ""

    while True:
        print(Fore.WHITE + "___________\n|         |\n|  _ _ _  |\n|_________|")

        print("Guess the first number")
        guess1 = get_num(1)
        
        print(Fore.WHITE + f"___________\n|         |\n|  {guess1} _ _  |\n|_________|")

        print("Guess the second number")
        guess2 = get_num(1)
        
        print(Fore.WHITE + f"___________\n|         |\n|  {guess1} {guess2} _  |\n|_________|")

        print("Guess the third number")
        guess3 = get_num(1)

        print(Fore.WHITE + f"___________\n|         |\n|  {guess1} {guess2} {guess3}  |\n|_________|")
        
        guessed_code = [guess1, guess2, guess3]
        print()
        slow_print(f"You entered: {guess1} {guess2} {guess3}")

        guess1_value = check_code_guess(guess1, door_code, 0)
        guess2_value = check_code_guess(guess2, door_code, 1)
        guess3_value = check_code_guess(guess3, door_code, 2)
        print()

        if guessed_code != door_code:
            slow_print(f"{guess1}: {guess1_value}")
            slow_print(f"{guess2}: {guess2_value}")
            slow_print(f"{guess3}: {guess3_value}")
            slow_print(Fore.RED + "___________\n| ACCESS  |\n| DENIED  |\n|_________|\n")
            slow_print("Better try again...")
            print()
        else:
            slow_print(Fore.GREEN + "___________\n| ACCESS  |\n| GRANTED |\n|_________|")
            print()    
            break


def avoid_asteroid():
    """Prompts the player to choose how to handle an oncoming asteroid

    Returns:
    ship_hit (bool): Whether the ship was hit (True) or not (False)
    """
    ship_hit = False

    while True:
        slow_print("You'll need to act fast. What do you want to do?")
        slow_print(Fore.CYAN + "    (1) Use your ship's boosters to try to quickly dodge the asteroid")
        slow_print(Fore.CYAN + "    (2) Shoot the asteroid with your ship's lasers")
        slow_print(Fore.CYAN + "    (3) Place your trust in your ship's shields and brace for impact.")

        ship_move = input("> ")
        print()

        if ship_move == "1":    # DODGE ASTEROID
            print("You quickly activate that ship's boosters and turn the ship as hard as you can to the right.\n")
            num = randint(1,3)
            if num == 1 or num == 2:
                slow_print("The asteroid just barely misses you, nearly taking out one of the ship's wings - but you're safe!\n")
                break
            else:
                slow_print("Despite your efforts, it's not enough and the asteroid partially collides with one of your ship's wings.\n")
                slow_print("You're going to need to make an emergency landing!\n")
                ship_hit = True
                break
        elif ship_move == "2":  # SHOOT ASTEROID
            print("You charge up the lasers, take aim at the asteroid, and fire several shots at it.\n")
            num = randint(1,2)
            if num == 1:
                slow_print("For a second you think you won't make it, but as you fire your last shot the asteroid explodes into tiny pieces right in front of you.\n")
                slow_print("There might be some superficial damage to the ship, but you're safe!\n")
                break
            else:
                slow_print("The asteroid remains intact, so you continue firing at it. It breaks up into slightly smaller pieces, but they hit you and are big enough to take parts of your ship out.\n")
                slow_print("You're going to need to make an emergency landing!\n")
                ship_hit = True
                break
        elif ship_move == "3":  # BRACE FOR IMPACT
            print("You divert all power to your ship's shield and take a deep breath as your ship and the asteroid head for impact.\n")
            num = randint(1,4)
            if num == 1:
                slow_print("The force of the impact nearly jolts you out of your seat, even with your seatbelt.\n")
                slow_print("You quickly check the dashboard and see that while your shields have taken damage, you're still in flying shape!\n")
                break
            else:
                slow_print("The force of the impact nearly jolts you out of your seat, even with your seatbelt.\n")
                slow_print("You check the dashboard and see numerous alerts popping up informing you of significant damage to the ship.\n")
                slow_print("You're going to need to make an emergency landing!\n")
                ship_hit = True
                break
        else:
            print("INVALID ENTRY: Must choose from available maneuvers (enter 1, 2, or 3)")
            print()
    
    return ship_hit


def escape_cell():
    """Player selects moves to make to try to escape the cell"""
    door_locked = True

    while door_locked == True:
        menu_level = 1
        slow_print("You're going to need to find a way to deal with that lock and get through the door.")
        slow_print(Fore.CYAN + "    (1) Try to break the lock.")
        slow_print(Fore.CYAN + "    (2) Look around the room for something helpful.")
        if "Skeleton Key" in inventory:
            slow_print(Fore.CYAN + "    (3) Use skeleton key.")

        tactic = input("> ")
        print()
        
        if tactic == "1":   # BREAK LOCK
            slow_print("You slip your hand through the metal bars of the door again, and this time you yank on the lock as hard as you can, but it doesn't give.")
            print()
        
        elif tactic == "2": # LOOK AROUND ROOM
            menu_level = 2
            slow_print("You search the dirt floor of the room, looking for something that could help you open the lock.\n")
            slow_print("You find... a stick. That lock did look pretty old. Maybe this could work?")
            slow_print(Fore.CYAN + "    (1) Take the stick and try using it on the lock")
            slow_print(Fore.CYAN + "    (2) Keep searching")
            
            while menu_level == 2:
                tactic = input("> ")
                print()

                if tactic == "1":   # TRY STICK
                    change_inventory("Stick", 1, "add")
                    print()
                    slow_print("You jam the stick into the lock and turn.\n")
                    slow_print("The stick breaks and you toss it on the ground.\n")
                    slow_print("Well, that didn't help.\n")
                    change_inventory("Stick", 1, "remove")
                    print()
                    menu_level = 1
                elif tactic == "2": # KEEP SEARCHING
                    menu_level = 3
                    slow_print("You don't have much hope in the stick, so you continue to search for something better.\n")
                    slow_print("You find... a rusty nail.")
                    slow_print(Fore.CYAN + "    (1) Take the rusty nail and try using it on the lock")
                    slow_print(Fore.CYAN + "    (2) Keep searching")

                    while menu_level == 3:
                        tactic = input("> ")
                        print()

                        if tactic == "1":   # TRY NAIL
                            change_inventory("Rusty Nail", 1, "add")
                            print()
                            slow_print("You try the nail in the lock.\n")
                            slow_print("You hear the sound of metal scraping against metal. You don't have much faith it will work...\n")
                            slow_print("Suddenly, the lock pops open.\n")
                            slow_print("You're free!\n")
                            slow_print("Well, you made it out of the room...\n")
                            slow_print("The nail, on the other hand, is stuck jammed into the lock. There's no way you're getting that back out.\n")
                            change_inventory("Rusty Nail", 1, "remove")
                            print()
                            menu_level = 0
                            door_locked = False
                        elif tactic == "2": # KEEP SEARCHING
                            slow_print("You continue to search the rest of the room.\n")
                            slow_print("You don't find anything else.\n")
                            menu_level = 1
                        else:
                            print("INVALID ENTRY: Must choose from available moves (enter 1 or 2)")
                else:
                    print("INVALID ENTRY: Must choose from available moves (enter 1 or 2)")

        elif tactic == "3" and "Skeleton Key" in inventory:
            slow_print("It's a struggle to get the key into the lock, but after wiggling it around for a bit the lock opens.\n")
            slow_print("You're free!\n")
            slow_print("Well, you made it out of the room...\n")
            menu_level = 0        
            door_locked = False
        
        elif tactic != "1" and tactic != "2" and tactic != "3" and "Skeleton Key" in inventory:
            print("INVALID ENTRY: Must choose from available moves (enter 1, 2, or 3)\n")
        
        else:
            print("INVALID ENTRY: Must choose from available moves (enter 1 or 2)\n")


def check_inventory(item):
    """Checks whether an item is in the player's inventory

    Returns:
    True/False (bool): True if item is in inventory, False if item is not in inventory
    """

    if item.title() in inventory:
        return True
    else:
        return False


def change_inventory(item, quantity, action):
    """ Adds or removes an item from the player's inventory and displays a confirmation message

    Parameters:
    item (str): Item to remove from inventory
    quantity (int): Amount to change inventory quantity by
    action (str): Whether to add or remove item
    """

    if action == "add":
        if item == "Funds":
            inventory[item] += quantity
            print(Fore.BLUE + f"    💸 + {quantity} Celestium")
        else:
            if item not in inventory:
                inventory[item] = 0
            inventory[item] += quantity
            print(Fore.BLUE + f"    📦 {item} added to inventory (+ {quantity})")

    elif action == "remove":
        if item == "Funds":
            inventory[item] -= quantity
            print(Fore.BLUE + f"    💸 - {quantity} Celestium")
        else:
            inventory[item] = max(0, (inventory[item] - quantity))
            if inventory[item] == 0:
                del inventory[item]
            print(Fore.BLUE + f"    📦 {item} removed from inventory (- {quantity})")


def show_inventory():
    """Prints a list of all items in the inventory and their quantities"""
    print(Fore.BLUE + "    - INVENTORY -")
    for key, value in inventory.items():
        if key == "Funds":
            print(Fore.BLUE + f"    {key}: {value} Celestium")
        else:
            print(Fore.BLUE + f"    {key}: {value}")


def display_funds():
    """Returns a string displaying the amount of money the player currently has"""

    return Fore.BLUE + f'    💰 FUNDS: {inventory["Funds"]} Celestium'


def show_shop_inventory(inventory):
    """Displays all items a shop has for sale (with prices and descriptions) for the player to select purchase
    
    Parameters:
    inventory (dict): Inventory list
    """
    print(Fore.CYAN + "    - SHOP INVENTORY -")
    i = 1
    for key in inventory:
        print(Fore.CYAN + f"    ({i}) {key}  ||  {inventory[key]['cost']} Celestium for {inventory[key]['quantity']}")
        # print(Fore.CYAN + f"        {inventory[key]['cost']} Celestium for {inventory[key]['quantity']}")
        print(Fore.CYAN + f"        {inventory[key]['description']}")
        i += 1
    print(Fore.CYAN + f"    ({i}) Nothing")


def purchase_item(item, quantity, cost):
    """Item purchase process

    Adds the item to player's inventory. Subtracts the cost from the player's funds. Display's player's current funds.

    Parameters:
    item (str): Item the player purchased
    cost (int): Cost of the item
    """

    change_inventory(item, quantity, "add")
    change_inventory("Funds", cost, "remove")
    print(f"{display_funds()}")
    

## SET UP DICTIONARIES

### Shop inventory (for shop on Mino)
mino_shop_inventory = {
    "Moon Food Meal Bar" : {
        "description" : "It's in your favorite flavor: Galactic S'mores!",
        "cost" : 7,
        "quantity" : 1,
        "purchase message" : "Always good to have one of these on hand."},
    "Skeleton Key" : {
        "description" : "It's old and rusty.",
        "cost" : 6,
        "quantity" : 1,
        "purchase message" : "It is pretty rusty but who knows, maybe it still has some life left in it."},
    "Glimmering Dagger" : {
        "description" : "You don't think you've ever seen a dagger so shiny.",
        "cost" : 12,
        "quantity" : 1,
        "purchase message" : "Hard to resist a dagger that pretty. And who couldn't use an extra self defense tool?"}
    }

### Weapons list
weapons = {
    "Supersonic Boltslinger" : {
        "description" : "Heavier, harder to aim, but very powerful",
        "chance" : 3,
        "damage" : 4},
    "Turbogun" : {
        "description" : "Lighter, easier to aim, but not as strong",
        "chance" : 2,
        "damage" : 2}
}

### Enemy list
enemies = {
    "Zimeon" : {
        "chance" : 3,
        "damage" : 2},
    "Hext" : {
        "chance" : 3,
        "damage" : 2}
}


### ACTUAL GAME ###
playing = True
# WELCOME
player_name = intro()
# player_name = "Jinx" # FOR TESTING ONLY

while playing == True:
    # (RE)SET UP VARIABLES
    inventory = {"Funds": 0}
    player_HP = 10
    spaceship_code = randint(1000, 10000)     # rand int that is 4 digits long
    door_code = generate_door_code(3)

    # TEMPORARY CODES FOR TESTING ONLY
    # spaceship_code = 1234
    # door_code = [1, 2, 3]

    # GAME START

    ## WAKE UP AT HOME
    slow_print("A beeping sound wakes you up and you open your eyes. You reach over to grab your holo-device from the nightstand next to your bed.\n")
    slow_print("As you turn off the alarm, you see that you have several notifications.\n")

    read_messages()

    slow_print("What a mixed bag of messages to wake up to. Despite the news of a potential return of the Isotropa, you're excited about getting to see Marz again. Luckily you didn't have plans today, so you can head over now!")
    print()

    while True:
        slow_print("How do you want to reply to Marz?")
        slow_print(Fore.CYAN + "    (1) omw, see u soon!!")
        slow_print(Fore.CYAN + "    (2) consider my ship's launch sequence initiated.")
        slow_print(Fore.CYAN + "    (3) 🤩 🚀 🔜")

        reply = input("> ")
        print()

        if reply == "1":
            reply_message = "omw, see u soon!!"
            break
        elif reply == "2":
            reply_message = "consider my ship's launch sequence initiated."
            break
        elif reply == "3":
            reply_message = "🤩🚀🔜"
            break
        else:
            print("INVALID ENTRY: Must choose from available message options (enter 1, 2, or 3)\n")


    slow_print("You type your reply:")
    typing("    ", 0, False)
    typing(Fore.GREEN + "TO: Marz", space=False)
    print()
    typing("    ", 0, False)
    typing(Fore.GREEN + f"{reply_message}", space=False)
    print()
    slow_print("And hit SEND.")

    print()
    slow_print("You quickly change clothes and fix your hair.\n")
    slow_print("As you grab your bag from where it's hanging off a chair, you notice your wallet on the table. Do you want to take it? [Y/N]")
    while True:
        take = input("> ").upper()
        print()
        if take == "Y":
            slow_print("Good thinking - you never know when you'll need some cash. You grab your wallet and put it in your bag.\n")
            sleep(1)
            change_inventory("Funds", 12, "add")
            print(display_funds())
            break
        elif take == "N":
            slow_print("You figure you'll be fine. You're just going to visit your friend.\n")
            sleep(1)
            print(display_funds())
            break
        else:
            print("INVALID ENTRY: Must enter Y or N")
    print()
    slow_print("Bag in hand, you head out the door and start walking towards your spaceship.")
    print()


    ## SHOP

    slow_print("As you're walking, you pass your local corner shop. Do you want to enter? [Y/N]")

    shop_entry = ""
    while shop_entry != "Y" and shop_entry != "N":
        shop_entry = input("> ").upper()
        print()

        if shop_entry == "Y":
            slow_print("You enter the shop and the shopkeeper invites you to take a look at what they're selling.\n")

            while True:
                slow_print("What do you want to buy?\n")
                sleep(1)
                print(f"{display_funds()}\n")
                show_shop_inventory(mino_shop_inventory)
                print()
                purchase = input("> ")
                print()

                if purchase == "1":
                    item_choice = "Moon Food Meal Bar"
                elif purchase == "2":
                    item_choice = "Skeleton Key"
                elif purchase == "3":
                    item_choice = "Glimmering Dagger"
                elif purchase == "4":
                    break
                else:
                    item_choice = False
                
                if item_choice == False:
                    print("You need to decide whether or not you want to purchase something (enter 1, 2, 3, or 4).")
                else:
                    if inventory["Funds"] >= mino_shop_inventory[item_choice]["cost"]:
                        print(mino_shop_inventory[item_choice]["purchase message"])
                        print()
                        sleep(1)
                        purchase_item(item_choice, mino_shop_inventory[item_choice]["quantity"], mino_shop_inventory[item_choice]["cost"])
                    else:
                        print(f"You don't have enough money for the {item_choice}!")
                print()
            print("You wave bye to the shopkeeper and leave.")

        elif shop_entry == "N":
            print("You decide not to step into the shop, eager to go see your friend. You wave at the shopkeeper as you pass by.")

        else:
            print("INVALID ENTRY: Must enter Y or N")
    print()

    ## GET ON SPACESHIP

    slow_print("You arrive at the spaceport and find your spaceship. You go inside and program the trip to Udreria, the planet where Marz lives.")
    print()
    slow_print("Before you can start your trip, you'll need to enter your launch code.")
    print()

    launch_spaceship(spaceship_code)

    print()
    slow_print("With the code entered, the launch sequence initiates. You settle into your chair for the journey.\n")


    ## SPACE TRAVEL & ASTEROID

    slow_print("Even with your many space travels, you're always awe struck by how beautiful space is.\n")

    slow_print("You watch the stars pass by and think about how tiny you are in the grand scheme of the galaxy.\n")

    slow_print("Your thoughts are interrupted by angry beeping. You check your monitor and see a flashing message in red text:\n")

    slow_print(Fore.RED + "    INCOMING ASTEROID\n")

    ship_hit = avoid_asteroid()
            

    ### EMERGENCY LANDING

    zimeon_alive = True
    if ship_hit == True:
        slow_print("You quickly steer your ship to land on the closest planet, Mophus, so that you can assess the damage and attempt repairs.\n")
        slow_print("You land in what appears to be an empty desert.\n")
        sleep(1)
        slow_print("Hit RETURN to open the door of your ship.")
        input("")
        slow_print("As the doors open, you're surprised to see someone standing there.\n")
        slow_print("It takes you a second before you recognize them - Zimeon, one of the leaders of the Isotropa faction.\n")
        slow_print("Behind them is a cage full of puppies. You remember this part of their tactics - these puppies have likely been taken hostage to be used as a bargaining chip.\n")
        slow_print(Fore.MAGENTA + "    💬 ZIMEON: You have excellent timing. My ship is having some issues, but it looks like yours could supply me with the parts I need. Are you going to hand it over peacefully or am I going to have to fight you for it?\n")
        slow_print("You reach for your gun holster. There's no way you're letting Zimeon take these puppies hostage AND scavenge your ship for parts.\n")

        weapon = choose_weapon()
        print()
        check_for_bar()
        print()
        zimeon_HP = 10
        sleep(1)

        while player_HP > 0 and zimeon_HP > 0:
            while True:
                print(f"Hit RETURN to fire your {weapon}!")
                move = input("")

                if move != "":
                    print()
                    item_status = check_inventory(move)
                    if item_status == True:
                        if player_HP <= 8:
                            player_HP = eat_bar_for_HP(player_HP)
                            break
                        else:
                            print("Your health is already completely full! You can't eat the bar now - if you do, it won't do anything.\n")
                    else:
                        print(f"Sorry, you don't have '{move}' in your inventory. You can't use something you don't have!\n")

                else:
                    zimeon_HP = player_attack(weapon, "Zimeon", zimeon_HP)
                    break
            
            if zimeon_HP > 0:
                player_HP = opponent_attack("Zimeon", player_HP)
            print()
        
        sleep(.5)
        typing("💥💥💥", time=0.3)
        print()
        sleep(.5)
        typing("☠️", time=0.3, space=False)
        print()
        print()
        sleep(.5)

        if zimeon_HP == 0:
            print("As you take your final shot, Zimeon sinks to the ground and keels over. You check for a pulse. Nothing. You shake your head. Looks like those news reports were substantiated after all. You hope Zimeon was acting on their own and not with a larger group of people...")
            zimeon_alive = False

        elif player_HP == 0:
            playing = player_died("Despite your bravery and strategic maneuvers, Zimeon overpowered you and won the fight.")
            print()
            continue

        print()
        slow_print("You release the puppies. After checking that they're all okay, you walk back to your ship.\n")
        slow_print("You grab your repair kit from your ship and get to work.\n")
        slow_print("You eventually complete the repairs and get back in your ship.\n")
        slow_print("You go back into your spaceship, still trying to process the sudden turn this trip has taken. You'll have plenty to talk about with Marz when you finally see them.\n")
        slow_print("Enter your launch code again to take off.\n")

        launch_spaceship(spaceship_code)

        print()
        slow_print("You settle back into your chair and set your ship to get back on course to Udreria.\n")
        slow_print("You pause for a moment to watch Mophus fade into the distance behind you.\n")
        slow_print("Hopefully this trip won't have any more unpleasant surprises.\n")


    ## ARRIVE ON UDRERIA
    slow_print("Wow, what a close call. You're grateful to have made it out of that in one piece!\n")

    if zimeon_alive == False and player_HP < 10:
        slow_print("Now that you have a moment of calm, you tend to your wounds from your battle with Zimeon.\n")
        healed_HP = 10 - player_HP
        player_HP = 10
        print(Fore.BLUE + f"    + {healed_HP} HP")
        print(Fore.BLUE + f"    YOUR HEALTH: {player_HP}\n")

    slow_print("It isn't long before you see Udreria growing closer.\n")
    slow_print("You steer your spaceship to a spaceport near where Marz lives and make your landing.\n")
    slow_print("Hit RETURN to open the door of your ship.")
    input("")
    slow_print("As the doors start to open, you think about how excited you are to see your friend.\n")
    slow_print("Once the doors are open, you step outside, smiling as rays from one of the Udreria's suns hit your face.\n")
    slow_print("Suddenly, you feel someone come up behind you and smother your face with a damp cloth. Your vision starts to go dark...\n")


    ## ESCAPE CELL
    sleep(1)
    typing("...", 3)
    print()
    print()
    print("You slowly open your eyes.\n")
    slow_print("You no longer feel sunshine on your face.\n")
    slow_print("Instead, you're sprawled out on the dirt floor of a dark room.\n")
    slow_print("And you have a pounding headache.\n")
    slow_print("You quickly check yourself for signs of injuries and are relieved to find none.\n")
    slow_print("However, you're troubled to find that you have neither of your guns on you.\n")
    slow_print("Well, at least whoever put you in here didn't think to search you too carefully. It looks like they didn't bother to empty your pockets.\n")
    slow_print("As you turn your head to look around you realize that one of the walls of the room has a barred door.\n")

    slow_print("Hit RETURN to try opening the door.")
    input("")

    slow_print("It doesn't budge.", .5)

    print()
    slow_print("Hit RETURN to try again.")
    input("")

    slow_print("Still nothing.\n", .5)
    slow_print("You're trapped. But by who? And why?\n")
    slow_print("You don't know what's going on but you have to get out.\n")
    slow_print("You look more closely at the door and as the fog in your head starts to clear, you see a lock on the outside. You reach your hands through the bar to try to get to the lock. You can just barely reach it, but you're able to give it a tug.\n")
    slow_print("Unsurprisingly, it's locked.")
    print()

    escape_cell()


    ## BREAK INTO MAIN ROOM
    slow_print("You step outside the room and find yourself in a long dark hallway.\n")
    slow_print("You pause for a moment, trying to figure out which direction to go.\n")
    slow_print("You realize you can make out voices in the distance and decide to follow them, having no other leads.\n")
    slow_print("After many twists and turns, you get to a hallway with a big door at the end of it.\n")
    slow_print("You sigh. Of course - another locked door.\n")
    slow_print("Then you realize the voices you followed are coming from beyond it. You think you can faintly make out Marz's voice!\n")
    slow_print("As you get closer to the door, you see that this is going to be more complicated than the cell door. This isn't the kind of door on which you can just pick the lock. In fact, there is no physical lock and no door handle. The blinking holo pad to the right of the door controls it, so you can't open the door manually.\n")
    slow_print("You'll have to enter the correct door code to get in.\n")
    
    sleep(1)
    guess_door_code()

    slow_print("You hear a series of beeps and the door slides open to reveal a large room.\n")


    ## FREE MARZ
    slow_print("The first thing you notice is Marz at the opposite end of the room - you feel a sense of relief upon seeing them.\n")
    slow_print("Then you realize that their hands and ankles are restrained.\n")
    slow_print("You look around the rest of the room and register the other three people there. One person is standing near Marz. The other two are standing next to each other, not far from where you stand in the doorway.\n")
    slow_print("All three of them are armed.\n")
    slow_print("You don't recognize any of them, but you do recognize the insignia on their uniforms - Isotropa. Of course.\n")
    slow_print("Everyone in the room stares back at you, each of them looking just as confused as you feel.\n")
    slow_print("The person standing closest to Marz is the first to break the silence.\n")
    slow_print(Fore.MAGENTA + "    💬 UNKNOWN ISOTROPA MEMBER 1: What are you doing here?! You're supposed to still be in that cell!\n")
    slow_print("They turn their angry gaze to the two people standing near you.\n")
    slow_print(Fore.MAGENTA + "    💬 UNKNOWN ISOTROPA MEMBER 1: Which of you is responsible for this? Some guards you two make...\n")
    slow_print("The two guards turn to face each other.\n")
    slow_print(Fore.MAGENTA + "    💬 UNKNOWN ISOTROPA GUARD 1: I told you to replace the lock on that cell door last week!\n")
    slow_print(Fore.MAGENTA + "    💬 UNKNOWN ISOTROPA GUARD 2: I didn't have time because I was too busy helping YOU learn how to use your new Supersonic Boltslinger! It's not MY fault you didn't put in the training hours earlier.\n")
    slow_print("You realize you have a small window of opportunity to arm yourself while the three of them bicker.\n")
    slow_print("From which Isotropa guard do you grab a gun?")
    while True:
        move = input("> ")
        print()
        if move  == "1":
            weapon = "Supersonic Boltslinger"
            break
        elif move == "2":
            weapon = "Turbogun"
            break
        else:
            print("INVALID ENTRY: Must choose from available options (enter 1 or 2)")
    slow_print("You move quickly, rushing forward and snatching a gun out of the holster of one of the Isotropa guards.\n")
    slow_print(f"You notice that it's a {weapon}. Well, at least it's a gun you're familiar with.\n")
    slow_print(Fore.BLUE + f"    💥 {weapon} equipped\n")
    slow_print("You aim it at the one who has done the most of the talking and is closest to Marz. It seems like they're the one in charge here.\n")
    slow_print("Or whatever passes for in charge with this crew, anyway...\n")
    slow_print("The presumed leader aims their gun at Marz. Out of the corner of your eye, you see the guard who still has their gun aim it at you.\n")
    slow_print(Fore.MAGENTA + "    💬 UNKNOWN ISOTROPA LEADER: Great, NOW look what a mess the two of you have made.\n")
    slow_print("There's a moment of tense silence...\n")
    sleep(2)
    slow_print("The leader focuses their gaze back on you.\n")
    slow_print(Fore.MAGENTA + "    💬 UNKNOWN ISOTROPA LEADER: Well, since you're here, I suppose it's nice to have you join us. I mean, it was almost comical how easy it was to get you to fall into our trap. We figured we could count on you to respond to a text from an old friend.\n")
    slow_print("You frown. They must have taken Marz's holo-device and sent the text themselves. That would explain the uncharacteristic mention of a surprise.\n")
    slow_print("You make a mental note to yourself: If a text from a friend seems off, maybe it means they've been taken hostage.\n")
    slow_print(Fore.MAGENTA + "    💬 UNKNOWN ISOTROPA LEADER: My apologies, let me introduce myself. My name is Hext, and those two over there are...friends of my own. We're here to seize control on behalf of the Isotropa.\n")
    slow_print(Fore.MAGENTA + "    💬 MARZ: It's just a handful of them! There's only these three here, and I heard them making a call to one another person about some puppies - I think the planet that that one is on is Mophus!\n")

    if zimeon_alive == False:
        slow_print("Zimeon! Jeez, what are the odds...\n")
        slow_print("At least that means you've already taken out a fourth of their faction, assuming it really was just the four of them.\n")

    slow_print("You try to do some mental calculations to see if you can take these three on.\n")
    slow_print(Fore.MAGENTA + f"    💬 HEXT: QUIET. I knew we should have put you in a cell of your own instead of having you here. Though the look on {player_name}'s face when the doors opened and they saw you may have made it worth it...\n")
    slow_print(Fore.MAGENTA + f"    💬 HEXT: Anyway, enough talking. Now that I have you two here, I can take you both out at once. And I'm going to start with you, {player_name}.\n")
    slow_print(Fore.MAGENTA + "    💬 HEXT: Guards, watch over Marz and make sure they don't try anything. I want to take this one on myself.\n")

    ## BATTLE HEXT
    # weapon = choose_weapon()
    # print()
    slow_print("The two guards rush over to Marz while the leader directs their aim at you.\n")
    check_for_bar()
    print()
    hext_HP = 10
    sleep(1)

    while player_HP > 0 and hext_HP > 0:
        while True:
            print(f"Hit RETURN to fire your {weapon}!")
            move = input("")

            if move != "":
                print()
                item_status = check_inventory(move)
                if item_status == True:
                    if player_HP <= 8:
                        player_HP = eat_bar_for_HP(player_HP)
                        break
                    else:
                        print("Your health is already completely full! You can't eat the bar now - if you do, it won't do anything.\n")
                else:
                    print(f"Sorry, you don't have '{move}' in your inventory. You can't use something you don't have!\n")

            else:
                hext_HP = player_attack(weapon, "Hext", hext_HP)
                break

        if hext_HP > 0:
            player_HP = opponent_attack("Hext", player_HP)
        print()

    sleep(.5)
    typing("💥💥💥", time=0.3)
    print()
    sleep(.5)
    typing("☠️", time=0.3, space=False)
    print()
    print()
    sleep(.5)

    if hext_HP == 0:
        slow_print("Your final shot hits Hext and they fall to the ground. As they start to take their last breaths, you quickly take out the two guards as well.")
    elif player_HP == 0:
        playing = player_died("Despite your bravery and strategic maneuvers, Hext overpowered you and won the fight.")
        print()
        continue
    print()

    slow_print(Fore.MAGENTA + "    💬 HEXT: You may have put up a good fight, but this isn't over...\n")
    slow_print("Hext takes one last labored breath and then... nothing. You check their pulse to make sure they're dead before searching their pockets until you find a set of keys.\n")
    slow_print("You run over to Marz and try several keys until you finally unlock their wrist and ankle restraints.\n")
    slow_print("You hug each other tightly. You don't think you've ever been as happy to hug them as you are in this moment.\n")
    slow_print("Well, there was the time you two took on The Order of the Legion...\n")
    slow_print("and that time with those Wildspears...\n")
    slow_print("but this is definitely a close third.\n")
    slow_print("As you two pull apart from your hug, you give Marz a questioning look.\n")
    slow_print(Fore.MAGENTA + "    💬 MARZ: Okay, you are not going to BELIEVE how this went down. Let's go get drinks and I'll tell you everything. You're in for a story.\n")
    if zimeon_alive == False:
        slow_print("You think back to your encounter with Zimeon. Marz's going to be in for a story as well.\n")
    slow_print("You and Marz link arms and walk together to your favorite tavern in all of Udreria: The Vagabond Rocheodian.\n")
    slow_print(Fore.MAGENTA + "    💬 MARZ: By the way, since you're here anyway: there is this mission I was just offered that I think you might want in on...\n")
    slow_print("As you two step out of the building you were in, you find yourself smiling as you once again feel the rays from one of Udreria's suns on your face.")

    print()
    print()
    sleep(2)
    typing("- TO BE CONTINUED -", space=False)
    print()
    print()
    sleep(1)
    playing = play_again()
    print()
print()
print()
game_credits()