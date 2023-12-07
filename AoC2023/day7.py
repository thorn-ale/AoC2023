from dataloader import get_input_data
from dataclasses import dataclass
from enum import IntEnum
from collections import defaultdict
from functools import reduce


class Values(IntEnum):
    FiveKind = 64
    FourKind = 32
    Full = 16
    ThreeKind = 8
    TwoPair = 4
    Pair = 2
    High = 1


@dataclass
class Hand:
    hand: str
    bet: int
    joker: bool

    def get_val(self) -> Values:
        return self.get_val_joker() if self.joker else self.get_val_no_joker()

    def get_val_no_joker(self) -> Values:
        hand_dict = defaultdict(int)
        for c in self.hand:
            hand_dict[c] += 1
        sort_val = sorted(hand_dict.values())
        if sort_val == [5]:
            return Values.FiveKind
        if sort_val == [1, 4]:
            return Values.FourKind
        if sort_val == [2, 3]:
            return Values.Full
        if max(sort_val) == 3:
            return Values.ThreeKind
        if sort_val[-2:] == [2, 2]:
            return Values.TwoPair
        if sort_val[-1] == 2:
            return Values.Pair
        return Values.High
    
    def get_val_joker(self) -> Values:
        if 'J' not in self.hand:
            return self.get_val_no_joker()
        hand_dict = defaultdict(int)
        for c in self.hand:
            hand_dict[c] += 1
        jk = hand_dict['J']
        sort_val = sorted([x for k, x in hand_dict.items() if k != 'J'])
        if jk == 5 or len(sort_val) == 1:
            return Values.FiveKind
        if jk + max(sort_val) == 4:
            return Values.FourKind
        if len(sort_val) == 2:
            return Values.Full
        if jk + max(sort_val) == 3:
            return Values.ThreeKind
        return Values.Pair
    
    def compare(self, other: 'Hand') -> int:
        #-1 => self < other
        # 0 => self = other
        # 1 => self > other
        if self.hand == other.hand:
            return 0
        sv = self.get_val()
        ov = other.get_val()
        if sv == ov:
            cards = 'J23456789TQKA' if self.joker else '23456789TJQKA'
            return -1 if [cards.index(c) for c in self.hand] < [cards.index(c) for c in other.hand] else 1
        return -1 if sv < ov else 1 
    
    def __eq__(self, other: 'Hand') -> bool:
        return self.compare(other) == 0
    
    def __lt__(self, other: 'Hand') -> bool:
        return self.compare(other) < 0
    
    def __le__(self, other: 'Hand') -> bool:
        return self.compare(other) <= 0
    
    def __gt__(self, other: 'Hand') -> bool:
        return self.compare(other) > 0
    
    def __ge__(self, other: 'Hand') -> bool:
        return self.compare(other) >= 0


def main():
    data = get_input_data(7).strip().split('\n')
    hands = sorted([Hand(h.split()[0], int(h.split()[1]), False) for h in data])
    # part 1 : 249483956
    print(reduce(int.__add__, [(i+1)*h.bet for i, h in enumerate(hands)]))

    hands = sorted([Hand(h.split()[0], int(h.split()[1]), True) for h in data])
    # part 2 : 252137472
    print(reduce(int.__add__, [(i+1)*h.bet for i, h in enumerate(hands)]))


if __name__ == '__main__':
    main()
