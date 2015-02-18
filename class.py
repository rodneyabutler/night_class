import random
   ##This is the class for the player character
class Player():
    def __init__(self, name, chest, persona, guile):
        self.name = name
        self.chest = chest
        self.persona = persona
        self.guile = guile
        self.alive = True

    def description(self):
        print "You are  {}, rising star and here are your noob stats: \nChest: {}\nPersona: {}\nGuile: {}".format(self.name, self.chest, self.persona, self.guile)
        print '-'*50
        print '-'*50

    def check_alive(self):
        if self.chest + self.persona + self.guile == 0:
            self.alive = False

  # the following class is the enemy class. There are three classes that are children of the
 # parent audience class
class Audience():
    def __init__(self):
        self.name = None
        self.size = None
        self.fervor = None
        self.intellect = None

    def __str__(self):
        return self.name


# Child class of Audience
class NRAAudience(Audience):
    def __init__(self):
        Audience.__init__(self)
        self.name = "Gunners"
        self.size = 1
        self.fervor = 2
        self.intellect = 3


class ProChoicers(Audience):
    def __init__(self):
        Audience.__init__(self)
        self.name = "Choicers"
        self.size = 4
        self.fervor = 5
        self.intellect = 6


class ProUnion(Audience):
    def __init__(self):
        Audience.__init__(self)
        self.name = "Unions"
        self.size = 7
        self.fervor = 8
        self.intellect = 9


class Geriatrics(Audience):
    def __init__(self):
        Audience.__init__(self)
        self.name = "Elderly"
        self.size = 4
        self.fervor = 5
        self.intellect = 6

        # print elderly (Tested)

#player = Player()
gunners = NRAAudience()
choicers = ProChoicers()
unions = ProUnion()
elderly = Geriatrics()
audlist = (gunners, choicers, unions, elderly)
      # I am using the audlist to call the enemy classes but it seem like the attributes ae not being seen.
challenger = random.choice(audlist)
print challenger
## print player

#These are the variables for the audience but they run tooo early.
#aud_name = raw_input("You have encountered a crowd of *what ever  aud group:")
#aud = Audience(aud_name, 50, 50, 50)
#aud.description


class Encounter(object):
    def __init__(self, player):
        self.player = player
        self.audlist = audlist

    def run_comparison(self):
        self.player.chest -= self.audlist.size
        self.player.persona -= self.audlist.fervor
        self.player.guile -= self.audlist.intellect


    # TODO: after the encounter, call the player's check alive
    # if they died at the encounter, the game is over
    # otherwise, continue to the next encounter


#I think I have removed the need for the code below
# def description(aud):
#     print "You, {}, must face a(n) audience of {} and here are their stats: \nSize: {}\nFervor: {}\nIntellect: {}".format(char_name, aud.type, aud.size, aud.fervor, aud.intellect)
#     print '-'*50
#     print '-'*50


def current_stats():
    print " Here are your stats for {}: \nChest: {}\nPersona:{}\nGuile:{}\n".format(char.name, char.chest, char.persona, char.guile)

def rep():
    char.chest +=100
    char.persona -=50
    char.guile +=200
    print "You have chosen Republican. {} you have encountered a group of {}".format(char_name, challenger)

def dem():
    char.chest +=150
    char.persona -=30
    char.guile +=100
    print "You have chosen Democrat. {} you have encountered a group of {}".format(char_name, challenger)

def ind():
    char.chest +=25
    char.persona +=100
    char.guile +=150
    print "You have chosen Independent.{} you have encountered a group of {}".format(char_name, challenger)

print '-'*50
print " You are an up and coming law student and you have clerked and interned for a number of entities now it is time for you to enter the fray and see where your future will go in politics. "
print '-'*50

char_name = raw_input("What is your politicians name?:")
char = Player(char_name, 50, 50, 50)
char.description()


def begin():
        print "What party do you want to be a member of?" \
              "1 = Republican" \
              "2 = Democrat" \
              "3 = Independent"
        print "-"*50
        print "-"*50
        class_choice = raw_input("Which party will you choose?")
        if class_choice == "1":
            rep()
        elif class_choice == "2":
            dem()
        elif class_choice == "3":
            ind()
        else:
                print'-'*50
                print "What? DO you want to be a green party member? Try again"
                print'-'*50
                begin()



begin()
current_stats()


#print " You,{} the {}, have encountered a group of {}".format(char_name,challenger)