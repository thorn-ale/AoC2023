from dataloader import get_input_data
from dataclasses import dataclass
import re


@dataclass
class Hand:
    red: int
    green: int
    blue: int

    def __le__(self, other: 'Hand') -> bool:
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue
    
    def pow(self) -> int:
        return self.red * self.green * self.blue


@dataclass
class Game:
    id: int
    rounds: list[Hand]
    config: Hand

    def is_possible(self) -> bool:
        return all([r <= self.config for r in self.rounds])
    
    def min_config(self) -> Hand:
        return Hand(
            max([h.red for h in self.rounds]),
            max([h.green for h in self.rounds]),
            max([h.blue for h in self.rounds]),
        )


def extract_nr(text: str, color: str) -> int:
    match = next(re.finditer(f'(\d+) {color}', text), 0)
    if match:
        return int(match.group(1))
    return 0


def parse_line(line: str, config: Hand) -> Game:
    id, game= line.split(':')
    return Game(
        int(id.split(' ')[1]),
        [Hand(extract_nr(p, 'red'), extract_nr(p, 'green'), extract_nr(p, 'blue')) for p in game.split(';')], 
        config
    )


def main():
    data = get_input_data(2)
    data = data.strip().split('\n')
    config = Hand(12, 13, 14)
    games = [parse_line(d, config) for d in data]

    # part 1 : 2617
    print(sum([x.id for x in games if x.is_possible()]))
    
    # part 2 : 59795
    print(sum([g.min_config().pow() for g in games]))


if __name__ == '__main__':
    main()
