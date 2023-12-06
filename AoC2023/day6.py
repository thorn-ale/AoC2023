from dataloader import get_input_data
from dataclasses import dataclass
from functools import reduce


@dataclass
class Race:
    time: int
    dist: int

    # len([_ for x in range(time) if x * (time - x) > dist])
    # => [_ for x in range(time) if -x^2 + x*time > dist]
    # => [_ for x in range(time) if -x^2 + x*time - dist > 0]
    # f(x) = -x^2 + x*time - dist ; solve for f(x) = 0
    # x1,2 = (-time +- sqrt(time^2 - 4 * -1 * -dist))/-2
    # all x as such as min(x1, x2) <= x <= max(x1, x2) is win condition
    
    def win(self) -> int:
        x1 = int((-self.time + (self.time**2 - 4*self.dist)**0.5) / -2)
        x2 = int((-self.time - (self.time**2 - 4*self.dist)**0.5) / -2)
        return abs(x1 - x2)


def main():
    data = get_input_data(6).strip().split('\n')

    # part 1 : 2344708
    print(reduce(int.__mul__, [r.win() for r in [Race(t, d) for t, d in zip(*[[int(x) for x in data[i].split()[1:] if x] for i in range(2)])]]))

    # part 2 : 30125202
    print(Race(*[int(data[i].split(':')[1].replace(' ', '')) for i in range(2)]).win())


if __name__ == '__main__':
    main()
