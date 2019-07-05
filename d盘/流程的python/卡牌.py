import collections

crad = collections.namedtuple('card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = '♥️，♦️，♣️，♠️'.split()
    def __init__(self):
        self.__card = [crad(rank, suit) for rank, suit in (self.ranks, self.suits)]


    def __len__(self):
        return len(self.__card)


    def __getitem__(self, item):
        return self.__card[item]
