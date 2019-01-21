# card objects

## 52-cards
## 4 suits: Spades, Hearts, Diamonds and Clubs

'''
♣ Clubs
♦ Diamonds
♥ Hearts
♠ Spades
'''

'''
Spades 􏰀→ 3 Hearts 􏰀→ 2 Diamonds 􏰀→ 1 Clubs 􏰀→ 0
Jack 􏰀→ 11 Queen 􏰀→ 12 King 􏰀→ 13
'''


class Card:
    '''
    standard playing card
    '''

    # class attributes (outside any method)
    suit_names = ['♣', '♦', '♥', '♠']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):  # the default card is 2 of clubs  2c
        self.suit = suit  # instance attribute
        self.rank = rank  # instance attribute

    def __str__(self):
        return ('%s of %s' % (Card.rank_names[self.rank],  # accessing class attributes
                              Card.suit_names[self.suit]))  # accessing class attributes

    # def __cmp__(self, other):
    #     # check the suits
    #     if self.suit > other.suit: return 1
    #     if self.suit < other.suit: return -1
    #
    #     # check the ranks
    #     if self.rank > other.rank: return 1
    #     if self.rank < other.rank: return -1
    #
    #     return 0

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


# create a card

queen_of_diamonds = Card(1, 12)
print(queen_of_diamonds)

queen_of_hearts = Card(2, 12)
print(queen_of_hearts)
print(queen_of_diamonds < queen_of_hearts)  # True

three_of_clubs = Card(0, 3)
three_of_spades = Card(3, 3)
print(three_of_clubs < three_of_spades)  # True


# Decks

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort(self):
        self.cards.sort()

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        #return '\n'.join(res)
        return ' ; '.join(res)

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

def find_defining_class(obj, method_name):
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':

    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))


    deck.move_cards(hand, 5)
    print("just print hand:", hand)
    hand.sort()
    print("sorted hand: ", hand)

# add, remove, shuffle and sort






