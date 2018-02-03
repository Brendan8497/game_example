# Brendan Ryan
# 11/2/2016
# Ex45

from sys import exit
from random import randint
from stats import luckCount
from stats import strength
from stats import stealth
from stats import intelligence

class Scene(object):

    def enter(self):
	print "This scene has not been made."
	exit(1) # ends the program

# Engine of the game.
class Engine(object):

    def __init__(self, scene_map):
	self.scene_map = scene_map

    # play function. Plays the game.
    def play(self):
        current_scene = self.scene_map.opening_scene() # defines the current scene as the opening scene

	while True:
            print "\n--------"
	    # name of the next is given the value of the enter function of the current scene's Class
            next_scene_name  =  current_scene.enter()
	    # The current scene is given the value of the next_scene_name's Class
            current_scene = self.scene_map.next_scene(next_scene_name)

# Death class
class Death(Scene):

    # random taunts are displayed when you die
    taunts = [
        "Better luck in the next life...",
        "RIP in Pepperoni",
        "Oh well, at least you tried.",
        "Just give up.",
        "It's okay, at least your mom still likes you.",
        "Just stop trying.",
        "A valiant effort, but a failure is a failure.",
    ]
        
    def enter(self):
	print Death.taunts[randint(0, len(self.taunts)-1)]
	exit(1)
	
class Intro(Scene):

    def enter(self):
        print "Thanks for playing The Adventure of Mount Spooky!"
        print ""
        print "Press 'Enter' to play. Press any other button to quit.\n"

        answer = raw_input("[INPUT] ")

        if (answer == ''):
            return 'stats_screen'

        else:
            return 'death'

class StatsScreen(Scene):

    def enter(self):
        print "Here are your stats.\n"

        print "Luck:", luckCount
        print "Strength:", strength
        print "Stealth:", stealth
        print "Intelligence:", intelligence

        raw_input("")

        return 'start_room'

class Home(Scene):

    def enter(self):
        print "You go back home defeated. You got scared and gave up on your dream"
        print "of becoming a treasure hunter. You become a blacksmith instead,"
        print "doomed to forever regret your cowardice. Congratulations, I guess."

        return 'death'

class StartRoom(Scene):

    def enter(self):
	print "You awake in a field under a starry sky. You get up and look around you."
	print "All you can see is Mount Spooky in the distance. You are hesitant to go,"
        print "but remember the only reason you are here is to find the lost treasure"
        print "you heard about that's supposed to be hidden in a cave somewhere on"
        print "Mount Spooky. Do you go forward to Mount Spooky or back home?\n"

        answer = raw_input("[INPUT] ")

        if (answer == 'Mount Spooky'):
            return 'goblin_room'

        elif (answer == 'Home'):
            return 'home'

class GoblinRoom(Scene):

    def enter(self):
	print "You head out towards Mount Spooky. By the time you reach the mountain"
	print "the sun has already started to rise. You look around for a while and find"
	print "a cave. You go in and see a goblin in the corner. What do you do?\n"
	print "A) Sneak Past Him"
	print "B) Charge Him"
	print "C) Talk to Him\n"

	answer = raw_input("[INPUT] ")

	if (answer == 'A'):
            if (stealth >= 30):
            
                print "You sneak past the Goblin without making a sound. You find a door"
                print "a little farther in the cave. You enter further into the cave."

                return 'spirit_room'

            else:

                print "You attempt to sneak past the Goblin, but he hears you and"
                print "stabs you in the back. You scream one last time before"
                print "your vision turns to black."

                return 'death'

        elif (answer == 'B'):
            if (strength >= 30):

                print "You charge the goblin and take him by surprise. You knock him"
                print "to the ground and knock him out with a rock."
                print "You proceed further into the cave and find a door. You enter"
                print "into the next room."

                return 'spirit_room'
            
            else:
                
                print "You charge the goblin and attempt to overpower him. He sees"
                print "you coming and pulls a rusty dagger from out of his loincloth."
                print "As you attempt to tackle him, he thrusts it into your stomach."
                print "You feel agonizing pain and then nothing as all fades to black."

                return 'death'

        elif (answer == 'C'):
            if (luckCount >= 85):
                print "You hail the goblin in Goblin Speech as you approach."
                print "He turns and hails you back, and you start a conversation."
                print "You ask him if there is any treasure in this cave.\n"

                if (luckCount >= 95):
                    print "The goblin pauses for a moment, then tells you to follow him."
                    print "He leads you through the cave, past ghosts and a dragon,"
                    print "beckoning for you to keep close. Finally he stops in"
                    print "front of another door and tells you this is where the treasure"
                    print "is hidden. You thank him and enter."

                    return 'treasure_room'
                
                else:
                    print "The goblin pauses for a moment, then tells you to follow him."
                    print "He leads you through the cave, past ghosts and a dragon,"
                    print "beckoning for you to keep close. Finally he stops in"
                    print "front of another door and tells you this is where the treasure"
                    print "is hidden. You thank him and enter.\n"

                    print "As you enter you realize the goblin lied to you."
                    print "You hear a lock click behind you and focus on what's ahead."
                    print "What's ahead is an army of goblins marching in the distance."
                    print "One of them sees you and directs the rest's attention to you."
                    print "A group of archers fire at you. An arrow hits you and you fall to"
                    print "the ground."

                    return 'death'

            elif (strength >= 30):
                print "You hail the goblin in Goblin Speech as you approach."
                print "He snarls at you and replies with a goblin speech curse word."
                print "He pulls a dagger from his loincloth and lunges at you."
                print "You dodge the attack and reverse the dagger towards him."
                print "He stabs himself and you advance further into the cave through"
                print "a door that you find in the back of the cave."

                return 'spirit_room'

            else:
                print "You hail the goblin in Goblin Speech as you approach."
                print "He snarls at you and replies with a goblin speech curse word."
                print "He pulls a dagger from his loincloth and stabs you. You die in"
                print "agonizing pain."

                return 'death'
            
			
class SpiritRoom(Scene):

    def enter(self):
	print "You are in an open area of the cave. It appears to be a goblim cemetery."
	print "You also see ghosts everywhere. You can't fight or talk to ghosts, and you're"
	print "not sure if they've noticed you or not. What do you do?\n"
	print "A) Walk Through the Graveyard"
	print "B) Sneak Past the Ghosts"
	print "C) Wait For a While"
	print "D) Attempt to Banish the Dead\n"

	answer = raw_input("[INPUT] ")

	if (answer == 'A'):

            if (luckCount >= 75 and stealth >= 75):

                print "You walk straight through the graveyard to a door at the other"
                print "end of the room. You reach the door undisturbed and enter."

                return 'dragon_room'

            else:

                print "You try to waltz through the graveyard with purpose, but the"
                print "ghosts notice you and start to wail. They start to crowd around you"
                print "and you are forced to endure the feeling of aging 1,000 years in"
                print "seconds. You turn to dust and cease to exist."

                return 'death'
            
        elif (answer == 'B'):

            if (stealth >= 75):

                print "You attempt to sneak past the ghosts, ducking and weaving"
                print "in and out of the shadows. The ghosts suspect nothing, and you"
                print "reach the door at the end of the room with ease. You enter into"
                print "the next room of the cave."

                return 'dragon_room'

            elif (luckCount >= 75):

                print "You are terrible at sneaking, but you try anyway. You end up"
                print "alerting a ghost or two as you clumsily make your way to"
                print "the end of the cave, but they leave you alone. Lucky you."
                print "You reach the door at the end of the room and enter."

                return 'dragon_room'

            else:

                print "You attempt to sneak past the ghosts, but trip over a grave"
                print "on your way to the back of the cave. Every ghost notices you"
                print "and crowds around you. You are forced to endure the feeling"
                print "of aging 1,000 years in seconds. You turn to dust and cease to exist."

                return 'death'

        elif (answer == 'C'):

            if (luckCount >= 50):

                print "You wait for a while and ghosts go away. You don't know when"
                print "they'll be back, so you hurry to the end of the room."
                print "You find a door and enter through it."

                return 'dragon_room'

            else:

                print "You wait a while, and eventually the ghosts detect you."
                print "They start to gather around you slowly, until there's a"
                print "mob of ghosts around you. They drain your life away until"
                print "there's nothing left of you but dust. You cease to exit."

                return 'death'

        elif (answer == 'D'):

            if (intelligence >= 80):

                print "You start to perform anti-necromancy magic that you"
                print "learned from watching mages in the Magic Guild."
                print "You finish the ritual and successfully banish the dead."
                print "You enter the next room."

                return 'dragon_room'

            elif (intelligence >= 60 and luckCount >= 80):

                print "You struggle to remember the anti-necromancy magic that"
                print "you watched the mages at the Magic Guild perform, but"
                print "nonetheless perform the ritual successfully. You"
                print "watch the ghosts banish and then proceed to the next room."

                return 'dragon_room'

            else:

                print "You attempt to perform anti-necromancy magic, but"
                print "don't know the proper spells. You end up killing yourself"
                print "and wake up as a ghost. You are doomed to roam the bowels of"
                print "Mount Spooky as a ghost forever."

                return 'death'
	    
class DragonRoom(Scene):

    def enter(self):
	print "As you enter the next room the first thing you feel is the heat."
	print "It feels like a furnace. You notice a few gold objects lying on the"
	print "floor all over the place, as well as huge sleeping dragon between you"
	print "and  the door at the other end of the cave. You are starting to notice"
	print "a pattern in the cave's architecture. You are convinced this is the cave"
	print "with the treasure. What do you do?\n"
	print "A) Sneak Past the Dragon"
	print "B) Kill the Dragon"
	print "C) Take Some Gold and Leave"
	print "D) Leave\n"

	answer = raw_input("[INPUT] ")

	if (answer == 'A'):

            if (stealth >= 90):

                print "You successfully sneak past the dragon. You look back once"
                print "you are at the door and see the dragon still sleeping."
                print "You quickly slip into the next room."

                return 'treasure_room'

            elif (luckCount >= 90):

                print "You somehow sneak past the dragon without waking it up."
                print "You are amazed at the outcome, but aren't going to complain."
                print "After a silent celebration, you slip into the next room."

                return 'treasure_room'

            elif (intelligence >= 90 and luckCount >= 50):

                print "The dragon wakes up due to your inability to sneak."
                print "Instead of panicking, you keep a level head and attempt to"
                print "speak to it with broken Dragon Speech, and he responds."
                print "He says he will grant you one thing if you agree to leave"
                print "and never come back. What do you ask for?\n"
                print "A) Gold"
                print "B) Survival"
                print "C) Knowledge"
                print "D) Refuse\n"

                answer = raw_input("[INPUT] ")

                if (answer == 'A'):

                    if (luckCount >= 90):
                        
                        print "The dragon curses your greed and gives you a golden sword."
                        print "He then tries to claw at you. You duck under his swipe and"
                        print "manage to flee.\n"

                        print "Congratulations, You Won! (Coward)"
                        exit(1)

                    if (strength >= 90):

                        print "The dragon curses your greed and gives you a golden sword."
                        print "He then tries to claw at you. You dodge his attack and"
                        print "thrust the golden sword you just received into the dragon's"
                        print "heart, killing it instantly. You proceed to the next room."

                        return 'treasure_room'

                    else:

                        print "The dragon curses your greed and gives you a golden sword."
                        print "He then tries to claw at you. His attack hits you, and you"
                        print "are sliced in two."

                        return 'death'

                elif (answer == 'B'):

                    print "He let's you leave with your life under the condition"
                    print "you never return. You agree and flee with haste."
                    print "You gain no wealth and waste your life wondering what"
                    print "could have been."

                    return 'death'

                elif (answer == 'C'):

                    print "He gives you a thick, dusty tome that he claims"
                    print "contains ancient magic. He then tries to claw at you."
                    print "You duck and fire a spell from the tome at the dragon."
                    print "A black and red arrow shoots from your hand towards the"
                    print "dragon. It goes through the dragon and it falls to the ground"
                    print "dead. You proceed to the next room."

                    return 'treasure_room'

                elif (answer == 'D'):

                    print "You refuse his offer and attack. You pick up a golden sword"
                    print "and duck under his claws."

                    if (strength >= 90):

                        print "You stab the dragon in the heart, killing him"
                        print "instantly. You rest for a while, then proceed to"
                        print "the next room."

                        return 'treasure_room'

                    else:

                        print "You attempt to lunge at the dragon, but you are incinerated"
                        print "in a blast of the dragon's flames."

                        return 'death'

            else:

                print "You wake the dragon up attempting to sneak past it. You"
                print "notice it's eyelid's slowly open as you are standing right"
                print "in front of it's face. It yawns as you try to run, then"
                print "blasts you with fire. You are burnt to cinders."

                return 'death'
            
        elif (answer == 'B'):

            if (strength >= 90):

                print "You pick up a golden sword and stab the dragon in the"
                print "heart, killing him instantly. You rest for a while, then proceed to"
                print "the next room."

                return 'treasure_room'

            elif (intelligence >= 90):

                print "You mutter a curse of death towards the dragon, and suddently"
                print "the soft sound of snoring slows down and stops. The dragon"
                print "has ceased to breath, and you enter the next room."

                return 'treasure_room'

            else:

                print "You lack the strength and experience to take on a dragon."
                print "You slash at it's scaly arm with a golden sword you found"
                print "on the ground and wake it up. It glares down at you and"
                print "swiftly eats you."

                return 'death'

        elif (answer == 'C'):

            if (stealth >= 75):

                print "You hastily and stealthily pocket some gold coins and pick up"
                print "some golden artifacts. You leave with a small fortune, and are able"
                print "to live a comfortable life.\n"

                print "Congratulations, You Won!"
                exit(1)

            elif (luckCount >= 75):

                print "You hastily pocket some gold coins and pick up"
                print "some golden artifacts. You leave with a small fortune, and are able"
                print "to live a comfortable life.\n"

                print "Congratulations, You Won!"
                exit(1)

            else:

                print "You start picking up golden artifacts noisily. You wake up the dragon"
                print "and stand in fear as it stares at you. It finally decides to eat you."

                return 'death'

        elif (answer == 'D'):

            return 'home'

class TreasureRoom(Scene):

    def enter(self):

        print "The room is filled with treasure. Gold, silver, gems of all kinds,"
        print "and various other artifacts litter the room. Literally mountains of"
        print "gold coins pile up against the cave walls. You stare in incredulity."
        print "It is then you realize you were born to be a Treasure Hunter."
        print "You take as much as you can carry back with you, and use the"
        print "money you earned to fund multiple expeditions back to Mount"
        print "Spooky.\n"

        print "Congratulations, You Won!"
        exit(1)

class Map(object):

    # creates a dictionary of the map.
    scenes = {
        'intro': Intro(),
        'stats_screen': StatsScreen(),
        'home': Home(),
        'start_room': StartRoom(),
        'goblin_room': GoblinRoom(),
        'spirit_room': SpiritRoom(),
        'dragon_room': DragonRoom(),
        'treasure_room': TreasureRoom(),
        'death': Death()
    }
	
    # the __init__ function
    def __init__(self, start_scene):
	self.start_scene = start_scene

    # next_scene function that returns the next scene in the game.
    def next_scene(self, scene_name):
	return Map.scenes.get(scene_name)

    # returns the opening scene of the game.
    def opening_scene(self):
	return self.next_scene(self.start_scene)

a_map = Map('intro')
a_game = Engine(a_map)
a_game.play()
