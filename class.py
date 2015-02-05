

class Player():
    def __init__(self, name, chest, persona, guile):
        self.name = name
        self.chest = chest
        self.persona = persona
        self.guile = guile


    def description(self):
        print "You are a politician {} and here are your stats: \nChest: {}\nPersona: {}\nGuile: {}".format(self.name, self.chest, self.persona, self.guile)
        print '-'*50
        print '-'*50

class Audience():
    def __init__(self, type, size, fervor, intellect):
        self.type = type
        self.size = size
        self.fervor = fervor
        self.intellect = intellect


    def description(self):
        print "You, Politician, must face a(n) {} audience and here are their stats: \nType: {}\nSize: {}\nIntellect: {}".format(self.type, self.size, self.fervor, self.intellect)
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

#gunrights = ("")
#prochoice
#unions
#geriatrics





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