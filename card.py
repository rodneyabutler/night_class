import _random
class Card(object):
    suits = ("Clubs", "Hearts", "Spades", "Diamonds")
    pips = ("2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace")

    def __init__(self, pip, suit):
        self.pip=pip
        self.suits=suits

    def __str__(self):
        return "%s %s"(self.pip, self.suits)