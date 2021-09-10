"""
For this problem you will build classes to simulate a deck of normal playing cards (using classes, obviously)

The Deck class needs the following interfaces:
The init method for this class should create a standard deck of 52 playing cards.
A cards attribute to keep track of the cards currently in the deck
A shuffle method that randomly shuffles the cards currently contained in it's deck
(There are a lot of card shuffling programming examples online you should be able to find to help with this)
A deal method that takes a single integer to indicate how many cards to deal, and returns those cards and removes
them from the deck. If more cards are requested than are in the deck then deal as many as possible.
A refill method that returns the deck to being a full deck of 52 cards
Additionally, implement a str method that in someway displays the face and suits of the cards contained in the deck
from top to bottom.

The Card class needs the following interfaces:
An init method that takes a suit and face for the card
A face attribute indicating what card face this is (e.g. "k" for king, "4" for 4)
A suit attribute indicating what suit this card is (e.g. "spade", "diamond")
A str method that displays the face and suit in a human readable manner when the card is printed.
"""


class Deck:
    def __init__(self):
        self.cards = None
        pass

    def shuffle(self):
        pass

    def refill(self):
        pass

    def deal(self, n):
        pass

    def __str__(self):
        pass


class Card:
    pass


"""
Stretch Project (Will be done depending on time constraints) (No tests for this one, have fun!)
Build a blackjack simulation (We won't even worry about betting)

Implement a Player Class that handles:
The player's current hand of cards
A player's name
The maximum value they are willing to hit based on their cards (e.g. This player plans to stop at 15)
A method to know if the player wants to hit or stand (i.e. get a card this round)
A str method to show the players current hand

An overarching Blackjack Class that implements:
An init method that takes a deck and a group of players
A start_game method that deals the players their initial cards
A do_round method that deals a card to all players that one one
A players_done method that returns if all players are done
A get_winner method that returns the current winner (Choose a any method needed to break a tie)
Finally, a str method that displays that state of all the players at any given time

Finally, implement a play_blackjack function that:
1. Creates a game with four people,
2. Iterates through each round of play until all players are complete, printing off the game status each round
3. Announces the winner

"""


class Player:
    pass


class Blackjack:
    pass


def play_blackjack():
    pass
