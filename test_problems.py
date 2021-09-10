from problems import Deck, Card


def test_deck():
    deck = Deck()
    assert len(deck.cards) == 52
    assert len(str(deck)) >= 104  # need at least two characters per card to display all cards
    before_shuffle = str(deck)
    deck.shuffle()
    assert str(deck) != before_shuffle  # long odds of this test being wrong
    hand = deck.deal(5)
    assert len(hand) == 5
    assert isinstance(hand[0], Card)
    assert len(deck.cards) == 47
    deck.refill()
    assert len(deck.cards) == 52
    assert len(set(card.suit for card in deck.cards)) == 4
    assert len(set(card.face for card in deck.cards)) == 13

