from sys import stdout, modules
from time import sleep
from random import randint, uniform

unicode_supported = False

if "idlelib" in modules:
    bag_contents = ["Beginner's Sword","Adventurer's Armour","Beginner's Shield"]
elif "idlelib" not in modules:
    unicode_supported = True
    bag_contents = ["Beginner's Sword\U0001F5E1","Adventurer's Armour\u26E8","Beginner's Shield\U0001F6E1"]
else:
    print("Something went wrong with the IDLE detector.")

player_hp = 10
exitprompt = False
trolls_killed = 0
ogres_escaped = 0
giants_escaped = 0
times_injured = 0

# this unicode character works because it only has 4 bytes 
# and IDLE only supports 4-byte unicode characters (in Python 3.6+)
player_hp_visual = "\u2764"

def typewrite(text):
    for i in text:
        stdout.write(i)
        stdout.flush()
        # random float number between 0.055 and 0.085
        # to make the typewriter look more human
        sleep(round(uniform(0.055, 0.095), 3))

typewrite("The Mystic Forest\n")
while True:
    # if players hp is 0 or less, they die
    if player_hp <= 0:
        typewrite("You have died.\n")
        typewrite("Your statistics:\n")
        print("Trolls killed: " + str(trolls_killed) + "\n" + "Ogres escaped: " + str(ogres_escaped) + "\n" + "Giants escaped: " + str(giants_escaped) + "\n" + "Times injured: " + str(times_injured))
        quit()
    option = str(input())
    if option == "0":
        typewrite("Your statistics:\n")
        print("Trolls killed: " + str(trolls_killed) + "\n" + "Ogres escaped: " + str(ogres_escaped) + "\n" + "Giants escaped: " + str(giants_escaped) + "\n" + "Times injured: " + str(times_injured))
        quit()
    elif option == "1":
        typewrite("Bag contents:\n")
        if len(bag_contents) == 0:
            typewrite("Your bag is empty.\n")
        else:
            for item in bag_contents:
                print(item)
    elif option == "2":
        dice_roll = randint(1,6)
        typewrite("You rolled a " + str(dice_roll) + ".\n")
        if dice_roll == 1:
            typewrite("You are fighting a troll.\n")
            # if player has sword, kill the troll and break the sword. if player doesn't have sword, lose 2 hp.
            if "Beginner's Sword\U0001F5E1" or "Beginner's Sword" in bag_contents:
                typewrite("You killed the troll!\n")
                trolls_killed += 1
                if unicode_supported == True:
                    bag_contents.remove("Beginner's Sword\U0001F5E1")
                else:
                    bag_contents.remove("Beginner's Sword")
                typewrite("You broke the sword!\n")
            else:
                times_injured += 1
                player_hp -= 2
                if player_hp <= 0:
                    typewrite("You lost 2 hp. HP: 0.\n")
                else:
                    typewrite("You lost 2 hp. HP: " + " ".join(player_hp_visual*player_hp) + " .\n")
        elif dice_roll == 2:
            typewrite("You are fighting an ogre.\n")
            # if player has shield, escape the ogre and lose the shield. if player doesn't have shield, lose 3 hp.
            if "Beginner's Shield\U0001F6E1" or "Beginner's Shield" in bag_contents:
                typewrite("You escaped the ogre!\n")
                ogres_escaped += 1
                if unicode_supported == True:
                    bag_contents.remove("Beginner's Shield\U0001F6E1")
                else:
                    bag_contents.remove("Beginner's Shield")
                typewrite("You lost the shield!\n")
            else:
                times_injured += 1
                player_hp -= 3
                if player_hp <= 0:
                    typewrite("You lost 3 hp. HP: 0.\n")
                else:
                    typewrite("You lost 3 hp. HP: " + " ".join(player_hp_visual*player_hp) + " .\n")
        elif dice_roll == 3:
            typewrite("You are fighting a giant.\n")
            # if player has armour, escape the giant and lose the armour. if player doesn't have armour, lose 4 hp.
            if "Adventurer's Armour\u26E8" or "Adventurer's Armour" in bag_contents:
                typewrite("You escaped the giant!\n")
                giants_escaped += 1
                if unicode_supported == True:
                    bag_contents.remove("Adventurer's Armour\u26E8")
                else:
                    bag_contents.remove("Adventurer's Armour")
                typewrite("You lost the armour!\n")
            else:
                times_injured += 1
                player_hp -= 4
                if player_hp <= 0:
                    typewrite("You lost 4 hp. HP: 0.\n")
                else:
                    typewrite("You lost 4 hp. HP: " + " ".join(player_hp_visual*player_hp) + " .\n")
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
                typewrite("You gained 3 hp. HP: " + " ".join(player_hp_visual*player_hp) + " .\n")
            elif player_hp == 8:
                player_hp += 2
                typewrite("You gained 2 hp. HP: " + " ".join(player_hp_visual*player_hp) + " .\n")
            elif player_hp == 9:
                player_hp += 1
                typewrite("You gained 1 hp. HP: " + " ".join(player_hp_visual*player_hp) + " .\n")
            else:
                typewrite("You already have 10 hp.\n")
        elif dice_roll == 6:
            # random item 1-3 is added to bag
            random_num = randint(1,3)
            if random_num == 1:
                typewrite("You found a sword!\n")
                if unicode_supported == True:
                    bag_contents.append("Beginner's Sword\U0001F5E1")
                else:
                    bag_contents.append("Beginner's Sword")
            elif random_num == 2:
                typewrite("You found armor!\n")
                if unicode_supported == True:
                    bag_contents.append("Adventurer's Armour\u26E8")
                else:
                    bag_contents.append("Adventurer's Armour")
            elif random_num == 3:
                typewrite("You found a shield!\n")
                if unicode_supported == True:
                    bag_contents.append("Beginner's Shield\U0001F6E1")
                else:
                    bag_contents.append("Beginner's Shield")