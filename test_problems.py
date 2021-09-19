from problems import Deck, Card


def test_deck():
    deck = Deck()
    assert len(deck.cards) == 52, "Deck should have 52 cards"
    assert len(str(deck)) >= 104, "Deck not displaying all cards"  # need at least two characters per card to display all cards
    before_shuffle = str(deck)
    deck.shuffle()
    assert str(deck) != before_shuffle, "Shuffling should change the order of cards"  # long odds of this test being wrong
    hand = deck.deal(5)
    assert len(hand) == 5, "Deal did not return 5 cards"
    assert isinstance(hand[0], Card), "Deal did not return Cards"
    assert len(deck.cards) == 47, "Deal did not remove the right number of cards from the deck"
    deck.refill()
    assert len(deck.cards) == 52, "Refill did not get the deck back to 52 cards"
    assert len(set(card.suit for card in deck.cards)) == 4, "Deck did not have 4 suits of cards"
    assert len(set(card.face for card in deck.cards)) == 13, "Deck did not have 13 values of cards"

