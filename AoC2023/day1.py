from dataloader import get_input_data
import re


def part1():
    data = get_input_data(1)
    numbers = []
    for line in data.strip().split('\n'):
        n = [x for x in line if x.isdigit()]
        numbers.append(int( n[0] + n[-1]))
    print(sum(numbers))


def part2():
    data = get_input_data(1)
    numbers = []
    for line in data.strip().split('\n'):
        n = []
        digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
        for i in range(len(line)):
            if line[i].isdigit():
                n.append(line[i])
            for d, v in digits.items():
                if d in line[i:min(i+len(d), len(line))]:
                    n.append(v[0])

        numbers.append(int( n[0] + n[-1]))
    print(sum(numbers))


if __name__ == '__main__':
    part1()
    part2()

