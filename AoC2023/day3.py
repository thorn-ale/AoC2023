from dataloader import get_input_data
from dataclasses import dataclass


@dataclass
class Vec:
    x: int
    y: int

    def __add__(self, other: 'Vec'):
        return Vec(self.x + other.x, self.y + other.y)


north, south = Vec(0, -1), Vec(0, 1)
east, west = Vec(1, 0), Vec(-1, 0)


@dataclass
class Symbol:
    pos: Vec
    value: str

    def adjacent(self, data: list[str]):
        adj_vals = []
        #look north:
        look_at = self.pos + north
        if look_at.y >= 0:
            acc = data[look_at.y][look_at.x]
            n_pos = look_at
            while 1:
                n_pos += east
                if n_pos.x >= len(data[0]):
                    break
                acc += data[n_pos.y][n_pos.x]
                if not acc[-1].isdigit():
                    break
            n_pos = look_at
            while 1:
                n_pos += west
                if n_pos.x < 0:
                    break
                acc = data[n_pos.y][n_pos.x] + acc
                if not acc[0].isdigit():
                    break
            adj_vals.extend([int(x) for x in acc.split('.') if x])
        
        #look south:
        look_at = self.pos + south
        if look_at.y < len(data):
            acc = data[look_at.y][look_at.x]
            n_pos = look_at
            while 1:
                n_pos += east
                if n_pos.x >= len(data[0]):
                    break
                acc += data[n_pos.y][n_pos.x]
                if not acc[-1].isdigit():
                    break
            n_pos = look_at
            while 1:
                n_pos += west
                if n_pos.x < 0:
                    break
                acc = data[n_pos.y][n_pos.x] + acc
                if not acc[0].isdigit():
                    break
            adj_vals.extend([int(x) for x in acc.split('.') if x])
        
        #look east
        look_at = self.pos + east
        if look_at.x < len(data[0]):
            acc = data[look_at.y][look_at.x]
            while acc[-1].isdigit():
                look_at += east
                if look_at.x >= len(data[0]):
                    acc += '.'
                    break
                acc += data[look_at.y][look_at.x]
            acc = acc[:-1]
            if acc:
                adj_vals.append(int(acc))

        #look west
        look_at = self.pos + west
        if look_at.x < len(data[0]):
            acc = data[look_at.y][look_at.x]
            while acc[0].isdigit():
                look_at += west
                if look_at.x < 0:
                    acc = '.' + acc
                    break
                acc = data[look_at.y][look_at.x] + acc
            acc = acc[1:]
            if acc:
                adj_vals.append(int(acc))
            
        return adj_vals
    
    def is_gear(self, data: list[str]) -> bool:
        return len(self.adjacent(data)) == 2
    
    def gear_ratio(self, data: list[str]) -> int:
        values = self.adjacent(data)
        if len(values) == 2:
            return int.__mul__(*values)
        return 0


def main():
    data = get_input_data(3).strip()
    rows = data.split('\n')
    symbols = [Symbol(Vec(j, i), v) for i, r in enumerate(rows) for j, v in enumerate(r)  if r and not v.isdigit() and v != '.']
    
    #part 1: 540131
    print(sum([y for x in symbols for y in x.adjacent(rows)]))

    #part 2: 86879020
    print(sum([x.gear_ratio(rows) for x in symbols]))


if __name__ == '__main__':
    main()
