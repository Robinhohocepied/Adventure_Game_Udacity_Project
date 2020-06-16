import time
import random



def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro(items, weapon_choice, creature_choice, runaway):
    creature_list = ["Fearless Orc","Fire Dragon", "Titan Crézus", "White Rhino"]
    creature = random.choice(creature_list)
    creature_choice.append(creature)
    print_pause("You find yourself standing in the frontier between an open field and a vast jungle.") 
    print_pause("Rumor has it that a " + creature_choice[0] +" is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you, 200 meters away, is a tiny abandoned house.")
    print_pause("To your right is a long path that leads to a secret sanctuary.")
    print_pause("In your hand you hold your dad's gift (old but gold), a small dagger.")


def house(items, weapon_choice, creature_choice, runaway):
        weapon_list = ["Sword of Damocles","Crossbow of Robin Hood", "Axe of Gimlin", "Whip of Indiana Jones"]
        weapon = random.choice(weapon_list)
        weapon_choice.append(weapon)
        if 'house' in items:
            print_pause("You have rummaged all the wedges of this house.. all you see is dust from termite mounds to spiders' webs.")
            print_pause("You carefuly walk back to the open fiel with the "+ weapon_choice[0]+".\n")
        else: 
            print_pause("You slowly approach the courtyard of the tiny house.")
            print_pause("You try to see if any window can let your gaze in.. but as expected all the windows and doors look barred.")
            print_pause("After several minutes you ought to force one of the doors with the dagger.")
            print_pause("GLING! CLIC! The door opens!")
            print_pause("You enter the house.. and as soon as you see no danger lies in it, you rapidly hunt for a better weapon.")
            print_pause("And on your left, under a piece of unshrunken cloth, you find the " + weapon_choice[0] + "... Lucky you!")
            print_pause("You walk back out to the field.\n")
            items.append("house")
        game_start(items, weapon_choice, creature_choice, runaway)

def sanctuary(items, weapon_choice, creature_choice, runaway):
    if not runaway:
        print_pause("After a 4 hour walk in the mountains of Zagros, near the vast plain of Mesopotamia, you reach what you think is the.. mighty sanctuary.")
        if not weapon_choice:
            print_pause("With precaution, you take your small dagger and move toward the small monument...")
        else:
            print_pause("With precaution, you take the "+ weapon_choice[0] +" and move toward the small monument...")
        print_pause("As you reach the sanctuary.. you start sensing the danger..") 
        print_pause("ROAAAAR! A "+creature_choice[0]+" jumps from a rock!")
        print_pause("Your eyes can't see anything else besides the " + creature_choice[0] + " that lies in front of you.")
        if not weapon_choice:
            print_pause("You feel completely unprepared for this fight.. your tiny dagger won't save you this time...")
        else:
            print_pause("The "+ weapon_choice[0] +" seems to be what the beast fears the most...\n")
        sanctuary_choice(items, weapon_choice, creature_choice, runaway)
    else:
        print_pause("You need to free the people of Mesopotamia from this terrible beast.")
        print_pause("You then decide to go back to the sanctuary to attempt to kill it..\n")
        print_pause("As you reach the sanctuary.. you hide behind some rocks and keep watching it..")
        print_pause("After 1 hour you get caught by the " +creature_choice[0]+ ". You have to face it again! Fear is in the air..\n" )
        sanctuary_choice(items, weapon_choice, creature_choice, runaway)

def sanctuary_choice(items, weapon_choice, creature_choice, runaway):    
    battle_choice = input("What would you like to do?\n (1) Run away or (2) Fight the " +creature_choice[0]+ "\n")
    if battle_choice == '1':  
        field(items, weapon_choice, creature_choice, runaway)

    elif battle_choice == '2':
        fight(items, weapon_choice, creature_choice, runaway)
    else:
        print_pause("The choice you have made does not allow to you to pursue the game..")
        sanctuary_choice(items, weapon_choice, creature_choice, runaway)
    

def field(items, weapon_choice, creature_choice, runaway):

    print_pause("As you see the " + creature_choice[0] + " you run without ever looking back..")
    print_pause("After 4 hours of running and hiding, you feel like you lost the "+creature_choice[0]+".")
    print_pause("You stand halfway from the sanctuary and the abandoned house.\n")
    runaway.append("runaway")
    game_start(items, weapon_choice, creature_choice, runaway)

def fight(items, weapon_choice, creature_choice, runaway):
    print_pause("\nYou decide to fight the " + creature_choice[0]+"!\n")
    if not weapon_choice:
        print_pause("The " + creature_choice[0]+" does not wait and attacks you!")
        print_pause("You fight back but the beast breaks your dagger and captures you!")
        print_pause("You have been defeated.. GAME OVER")
    else:
        print_pause("Your take out your "+ weapon_choice[0] +" and wound the "+ creature_choice[0]+" one time.. two times... three times..")
        print_pause("The "+ creature_choice[0]+" is down.. injured.. barely breathing.")
        print_pause("The beast is dead.. you win!!!")
    replay_game(items, weapon_choice, creature_choice, runaway)

def replay_game(items, weapon_choice, creature_choice, runaway):
        choice = input("What would you like to play again? (y/n) \n")
        if choice == 'y':  
            weapon_choice.clear()
            creature_choice.clear()
            runaway.clear()
            intro(items, weapon_choice, creature_choice, runaway)
            game_start(items, weapon_choice, creature_choice, runaway) 

        elif choice == 'n':
            print_pause("Thank you for playing! Arrivederci, a dopo.")
           
        else:
            print_pause("The choice you have made does not allow to you to pursue or quit the game.")
            replay_game(items, weapon_choice, creature_choice, runaway)

def game_start(items, weapon_choice, creature_choice, runaway):
    print_pause("Enter 1 to walk to the abandoned house.")
    print_pause("Enter 2 to take the path toward the sanctuary.\n")
    choice = input("What would you like to do?\n (Please enter 1 or 2) \n")

    if choice == '1':  
        house(items, weapon_choice, creature_choice, runaway) 

    elif choice == '2':
        sanctuary(items, weapon_choice, creature_choice, runaway)
    else:
        print_pause("The choice you have made does not allow to you to pursue the game..")
        game_start(items, weapon_choice, creature_choice, runaway)


def main():
    weapon_choice = []
    creature_choice = []
    items = []
    runaway = []
    intro(items, weapon_choice, creature_choice, runaway)
    game_start(items, weapon_choice, creature_choice, runaway)

main()
