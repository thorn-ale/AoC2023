from dataloader import get_input_data


def main():
    data = get_input_data(4).strip().split('\n')
    points = 0
    copies = [0] + [1] * len(data)
    for line in data:
        card, remain = line.split(':')
        card = int(card.split()[-1])
        win, nums = [set(x.strip().split()) for x in remain.split('|')]
        intersec = win.intersection(nums)
        points += int(2**(len(intersec)-1))
        for i in range(len(intersec)):
            copies[card+i+1] += copies[card]
    #part 1 : 27845
    print(points)
    # part 2 : 9496801
    print(sum(copies))


if __name__ == '__main__':
    main()
