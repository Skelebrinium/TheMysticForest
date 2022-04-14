import sys
sys.dont_write_bytecode = True
from time import sleep
from random import randint, uniform
from playsounds import playsound

unicode_supported = False

if "idlelib" in sys.modules:
    # IDLE has partial unicode support(up to 4-byte unicode characters) so \u26E8 works
    player_hp_visual = ["\u2764", "\u274C"]
    bag_contents = ["Beginner's Sword", "Adventurer's Armour\u26E8", "Beginner's Shield", "Silver Knife"]
    potion_bag_contents = []
else:
    unicode_supported = True
    player_hp_visual = ["\u2764", "\u274C"]
    bag_contents = ["Beginner's Sword\U0001F5E1", "Adventurer's Armour\u26E8", "Beginner's Shield\U0001F6E1", "Silver Knife\U0001F5E1"]
    potion_bag_contents = []

player_hp, exitprompt, trolls_killed, ogres_escaped, giants_escaped, times_injured, potions_used, werewolves_killed = (10, False, 0, 0, 0, 0, 0, 0)
attack_shields = 0

def typewrite(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        # random float number between 0.055 and 0.085
        # to make the typewriter look more human
        sleep(round(uniform(0.055, 0.095), 3))

def addCharUntilLength(text, length, char):
    # count the number of characters in the string and add the specified character until the string is the specified length. do not count whitespace
    count = 0
    while len(text) - text.count(" ") < length:
        if count == 0:
            text += " " + char
            count += 1
        else:
            text += char
    return text

typewrite("The Mystic Forest\n")
while exitprompt == False:
    # if players hp is 0 or less, they die
    if player_hp <= 0:
        typewrite("You have died.\n")
        typewrite("Your statistics:\n")
        print("Trolls killed: " + str(trolls_killed) + "\n" + "Ogres escaped: " + str(ogres_escaped) + "\n" + "Giants escaped: " + str(giants_escaped) + "\n" + "Times injured: " + str(times_injured) + "\n" + "Potions used: " + str(potions_used) + "\n" + "Werewolves killed: " + str(werewolves_killed))
        exitprompt = True
    else:
        option = str(input())
        # player can enter list of instructions and program will execute them all
        for character in option:
            # if players hp is 0 or less, they die
            if player_hp <= 0:
                typewrite("You have died.\n")
                typewrite("Your statistics:\n")
                print("Trolls killed: " + str(trolls_killed) + "\n" + "Ogres escaped: " + str(ogres_escaped) + "\n" + "Giants escaped: " + str(giants_escaped) + "\n" + "Times injured: " + str(times_injured) + "\n" + "Potions used: " + str(potions_used) + "\n" + "Werewolves killed: " + str(werewolves_killed))
                exitprompt = True
            if "0" in character:
                typewrite("Your statistics:\n")
                print("Trolls killed: " + str(trolls_killed) + "\n" + "Ogres escaped: " + str(ogres_escaped) + "\n" + "Giants escaped: " + str(giants_escaped) + "\n" + "Times injured: " + str(times_injured) + "\n" + "Potions used: " + str(potions_used) + "\n" + "Werewolves killed: " + str(werewolves_killed))
                exitprompt = True
            elif "1" in character:
                playsound("./sounds/open_bag.mp3", False)
                typewrite("Bag contents:\n")
                if len(bag_contents) == 0:
                    typewrite("Your bag is empty.\n")
                else:
                    for item in bag_contents:
                        print(item)
            elif "2" in character:
                dice_roll = randint(1,7)
                playsound("./sounds/roll_dice.mp3", False)
                typewrite("You rolled a " + str(dice_roll) + ".\n")
                if dice_roll == 1:
                    typewrite("You are fighting a troll.\n")
                    # if player has sword, kill the troll and break the sword. if player doesn't have sword, lose 2 hp.
                    if "Beginner's Sword\U0001F5E1" in bag_contents:
                        playsound("./sounds/enemy_death.mp3", False)
                        typewrite("You killed the troll!\n")
                        trolls_killed += 1
                        bag_contents.remove("Beginner's Sword\U0001F5E1")
                        typewrite("You broke the sword!\n")
                    elif "Beginner's Sword" in bag_contents:
                        playsound("./sounds/enemy_death.mp3", False)
                        typewrite("You killed the troll!\n")
                        trolls_killed += 1
                        bag_contents.remove("Beginner's Sword")
                        typewrite("You broke the sword!\n")
                    else:
                        if attack_shields > 0:
                            attack_shields -= 1
                            typewrite("You lost 1 shield.\n")
                            typewrite("Remaining shields: " + str(attack_shields) + ".\n")
                        else:
                            times_injured += 1
                            player_hp -= 2
                            if player_hp <= 0:
                                playsound("./sounds/damage_taken.mp3", False)
                                typewrite("You lost 2 hp. HP: 0.\n")
                            else:
                                playsound("./sounds/damage_taken.mp3", False)
                                new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                                typewrite("You lost 2 hp. HP: " + new_player_hp_visual + " .\n")
                elif dice_roll == 2:
                    typewrite("You are fighting an ogre.\n")
                    # if player has shield, escape the ogre and lose the shield. if player doesn't have shield, lose 3 hp.
                    if "Beginner's Shield\U0001F6E1" in bag_contents:
                        playsound("./sounds/escape_enemy.mp3", False)
                        typewrite("You escaped the ogre!\n")
                        ogres_escaped += 1
                        bag_contents.remove("Beginner's Shield\U0001F6E1")
                        typewrite("You lost the shield!\n")
                    elif "Beginner's Shield" in bag_contents:
                        playsound("./sounds/escape_enemy.mp3", False)
                        typewrite("You escaped the ogre!\n")
                        ogres_escaped += 1
                        bag_contents.remove("Beginner's Shield")
                        typewrite("You lost the shield!\n")
                    else:
                        if attack_shields > 0:
                            attack_shields -= 1
                            typewrite("You lost 1 shield.\n")
                            typewrite("Remaining shields: " + str(attack_shields) + ".\n")
                        else:
                            times_injured += 1
                            player_hp -= 3
                            if player_hp <= 0:
                                playsound("./sounds/damage_taken.mp3", False)
                                typewrite("You lost 3 hp. HP: 0.\n")
                            else:
                                playsound("./sounds/damage_taken.mp3", False)
                                new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                                typewrite("You lost 3 hp. HP: " + new_player_hp_visual + " .\n")
                elif dice_roll == 3:
                    typewrite("You are fighting a giant.\n")
                    # if player has armour, escape the giant and lose the armour. if player doesn't have armour, lose 4 hp.
                    if "Adventurer's Armour\u26E8" in bag_contents:
                        playsound("./sounds/escape_enemy.mp3", False)
                        typewrite("You escaped the giant!\n")
                        giants_escaped += 1
                        bag_contents.remove("Adventurer's Armour\u26E8")
                        typewrite("You lost the armour!\n")
                    else:
                        if attack_shields > 0:
                            attack_shields -= 1
                            typewrite("You lost 1 shield.\n")
                            typewrite("Remaining shields: " + str(attack_shields) + ".\n")
                        else:
                            times_injured += 1
                            player_hp -= 4
                            if player_hp <= 0:
                                playsound("./sounds/damage_taken.mp3", False)
                                typewrite("You lost 4 hp. HP: 0.\n")
                            else:
                                playsound("./sounds/damage_taken.mp3", False)
                                new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                                typewrite("You lost 4 hp. HP: " + new_player_hp_visual + " .\n")
                elif dice_roll == 4:
                    typewrite("You found a thief!\n")
                    # if player has items in bag, thief steals first item
                    if len(bag_contents) > 0:
                        typewrite("The thief stole " + "'" + bag_contents[0] + "'" + "!" + "\n")
                        bag_contents.remove(bag_contents[0])
                    else:
                        typewrite("The thief stole nothing!\n")
                elif dice_roll == 5:
                    typewrite("You found a healer!\n")
                    # if player hp is 7 or less, add 3. if player hp is 8, add 2. if player hp is 9, add 1.
                    if player_hp <= 7:
                        player_hp += 3
                        new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                        typewrite("You gained 3 hp. HP: " + new_player_hp_visual + " .\n")
                    elif player_hp == 8:
                        player_hp += 2
                        playsound("./sounds/health_gain.mp3", False)
                        new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                        typewrite("You gained 2 hp. HP: " + new_player_hp_visual + " .\n")
                    elif player_hp == 9:
                        player_hp += 1
                        playsound("./sounds/health_gain.mp3", False)
                        new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                        typewrite("You gained 1 hp. HP: " + new_player_hp_visual + " .\n")
                    else:
                        typewrite("You already have 10 hp.\n")
                elif dice_roll == 6:
                    # random item 1-3 is added to bag
                    random_num = randint(1, 6)
                    if random_num == 1:
                        typewrite("You found a sword!\n")
                        if unicode_supported == True:
                            playsound("./sounds/new_item.mp3", False)
                            bag_contents.append("Beginner's Sword\U0001F5E1")
                        else:
                            playsound("./sounds/new_item.mp3", False)
                            bag_contents.append("Beginner's Sword")
                    elif random_num == 2:
                        typewrite("You found armour!\n")
                        playsound("./sounds/new_item.mp3", False)
                        bag_contents.append("Adventurer's Armour\u26E8")
                    elif random_num == 3:
                        typewrite("You found a shield!\n")
                        if unicode_supported == True:
                            playsound("./sounds/new_item.mp3", False)
                            bag_contents.append("Beginner's Shield\U0001F6E1")
                        else:
                            playsound("./sounds/new_item.mp3", False)
                            bag_contents.append("Beginner's Shield")
                    elif random_num == 4:
                        typewrite("You found a silver knife!\n")
                        playsound("./sounds/new_item.mp3", False)
                        if unicode_supported == True:
                            bag_contents.append("Silver Knife\U0001F5E1")
                        else:
                            bag_contents.append("Silver Knife")
                    elif random_num == 5:
                        typewrite("You found a health potion!\n")
                        playsound("./sounds/new_item.mp3", False)
                        potion_bag_contents.append("Health Potion\u2764")
                    elif random_num == 6:
                        typewrite("You found a shield potion!\n")
                        playsound("./sounds/new_item.mp3", False)
                        potion_bag_contents.append("Shield Potion\u26E8")
                elif dice_roll == 7:
                    typewrite("You are fighting a werewolf!\n")
                    # if player has silver knife, kill the werewolf and lose the knife. if player doesn't have silver knife, lose 4 hp.
                    if "Silver Knife\U0001F5E1" in bag_contents:
                        playsound("./sounds/enemy_death.mp3", False)
                        typewrite("You killed the werewolf!\n")
                        werewolves_killed += 1
                        bag_contents.remove("Silver Knife\U0001F5E1")
                        typewrite("You lost the silver knife!\n")
                    elif "Silver Knife" in bag_contents:
                        playsound("./sounds/enemy_death.mp3", False)
                        typewrite("You killed the werewolf!\n")
                        werewolves_killed += 1
                        bag_contents.remove("Silver Knife")
                        typewrite("You lost the silver knife!\n")
                    else:
                        if attack_shields > 0:
                            attack_shields -= 1
                            typewrite("You lost 1 shield.\n")
                            typewrite("Remaining shields: " + str(attack_shields) + ".\n")
                        else:
                            times_injured += 1
                            player_hp -= 4
                            if player_hp <= 0:
                                playsound("./sounds/damage_taken.mp3", False)
                                typewrite("You lost 4 hp. HP: 0.\n")
                            else:
                                playsound("./sounds/damage_taken.mp3", False)
                                new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                                typewrite("You lost 4 hp. HP: " + new_player_hp_visual + " .\n")
            elif "3" in character:
                # potion bag
                playsound("./sounds/open_bag.mp3", False)
                typewrite("Potion Bag contents:\n")
                if len(potion_bag_contents) == 0:
                    typewrite("Your potion bag is empty.\n")
                else:
                    for item in potion_bag_contents:
                        print(item)
                    potion_choice = str(input("What potion would you like to use? "))
                    # if player chooses health potion, add 4 hp and remove potion from potion bag
                    if potion_choice in ["Health Potion", "hp", "HP", "health", "Health", "health potion", "Health potion"]:
                        if "Health Potion\u2764" in potion_bag_contents:
                            if player_hp == 10:
                                typewrite("You already have 10 hp.\n")
                            else:
                                player_hp += 4
                                potion_bag_contents.remove("Health Potion\u2764")
                                playsound("./sounds/health_gain.mp3", False)
                                new_player_hp_visual = addCharUntilLength(" ".join(player_hp_visual[0] * player_hp), 10, player_hp_visual[1])
                                typewrite("You gained 4 hp. HP: " + new_player_hp_visual + " .\n")
                                potions_used += 1
                            if player_hp > 10:
                                player_hp = 10
                        else:
                            typewrite("You don't have a health potion.\n")
                    # if player chooses shield potion, add make next attack do no damage and remove potion from potion bag
                    elif potion_choice in ["Shield Potion", "Shield", "shield", "Shield potion", "shield potion"]:
                        if "Shield Potion\u26E8" in potion_bag_contents:
                            if attack_shields == 3:
                                typewrite("You can only have 3 attack shields at once.\n")
                            else:
                                attack_shields += 1
                                potion_bag_contents.remove("Shield Potion\u26E8")
                                playsound("./sounds/shield_gain.mp3", False)
                                typewrite("You gained a shield.\n")
                                typewrite("Remaining shields: " + str(attack_shields) + ".\n")
                                potions_used += 1
                        else:
                            typewrite("You don't have any shield potions.\n")
                    else:
                        typewrite("That is not a potion.\n")
            else:
                print("That is not a correct command.")
