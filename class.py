import random

class Player():
    def __init__(self, name, chest, persona, guile): #self.name is also used by the audience class
        self.name = name
        self.chest = chest
        self.persona = persona
        self.guile = guile


    def description(self):
        print "You are a politician {} and here are your stats: \nChest: {}\nPersona: {}\nGuile: {}".format(self.name, self.chest, self.persona, self.guile)
        print '-'*50
        print '-'*50

class Audience():
    def __init__(self, name, size, fervor, intellect):
        self.name = name
        self.size = size
        self.fervor = fervor
        self.intellect = intellect
#I need a variable to group all of the groups. Can I make a list of variables?


def nra():
    aud.name = "NRA gun enthusiasts"
    aud.size = 1
    aud.fervor = 2
    aud.intellect = 3

def choice():
    aud.name = "Pro Choicers"
    aud.size = 4
    aud.fervor = 5
    aud.intellect = 6

def union():
    aud.name = "Union Members"
    aud.size = 7
    aud.fervor = 8
    aud.intellect = 9

def geriatrics():
    aud.name = "Old Folks"
    aud.size = 10
    aud.fervor = 11
    aud.intellect = 12
#These are the variables for the audience but they run tooo early.
#aud_name = raw_input("You have encountered a crowd of *what ever  aud group:")
#aud = Audience(aud_name, 50, 50, 50)
#aud.description


def description(aud):
    print "You, Politician, must face a(n) audience of {} and here are their stats: \nSize: {}\nFervor: {}\nIntellect: {}".format(aud.type, aud.size, aud.fervor, aud.intellect)
    print '-'*50
    print '-'*50


def current_stats():
    print " Here are your stats for {}: \nChest: {}\nPersona:{}\nGuile:{}\n".format(char.name, char.chest, char.persona, char.guile)

def rep():
    char.chest +=100
    char.persona -=50
    char.guile +=200
    print "You have chosen Republican..."

def dem():
    char.chest +=150
    char.persona -=30
    char.guile +=100
    print "You have chosen Democrat..."

def ind():
    char.chest +=25
    char.persona +=100
    char.guile +=150
    print "You have chosen Independent..."

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