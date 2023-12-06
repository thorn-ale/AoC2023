from dataloader import get_input_data
from dataclasses import dataclass


@dataclass
class MapItem:
    dst: int
    src: int
    rng: int


def get_dest(items: list[MapItem], src: int) -> int|float:
    for item in items:
        if src >= item.src and src < item.src + item.rng:
            return item.dst + src - item.src
    return src


def get_src(items: list[MapItem], dest: int) -> int|float:
    for item in items:
        if dest >= item.dst and dest < item.dst + item.rng:
            return item.src + dest - item.dst
    return dest


def main():
    data = get_input_data(5).strip().split('\n\n')
    seeds = [int(x) for x in data[0].split(': ')[1].split() if x.strip()]
    seed_to_soil = [MapItem(*[int(i) for i in x.split()]) for x in data[1].split('\n')[1:]]
    soil_to_fert = [MapItem(*[int(i) for i in x.split()]) for x in data[2].split('\n')[1:]]
    fert_to_water = [MapItem(*[int(i) for i in x.split()]) for x in data[3].split('\n')[1:]]
    water_to_light = [MapItem(*[int(i) for i in x.split()]) for x in data[4].split('\n')[1:]]
    light_to_temp = [MapItem(*[int(i) for i in x.split()]) for x in data[5].split('\n')[1:]]
    temp_to_humid = [MapItem(*[int(i) for i in x.split()]) for x in data[6].split('\n')[1:]]
    humid_to_loc = [MapItem(*[int(i) for i in x.split()]) for x in data[7].split('\n')[1:]]

    def seed_to_loc(_seed: int) -> int:
        return get_dest(humid_to_loc, 
            get_dest(temp_to_humid, 
            get_dest(light_to_temp, 
            get_dest(water_to_light, 
            get_dest(fert_to_water, 
            get_dest(soil_to_fert, 
            get_dest(seed_to_soil, _seed)))))))

    # part 1 : 600279879
    print(min(seed_to_loc(seed) for seed in seeds))

    def loc_to_seed(_seed: int) -> int:
        return get_src(seed_to_soil, 
            get_src(soil_to_fert, 
            get_src(fert_to_water, 
            get_src(water_to_light, 
            get_src(light_to_temp, 
            get_src(temp_to_humid,
            get_src(humid_to_loc, _seed)))))))
    

    seed_ranges = [range(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
    loc = 0
    found = False
    # good idea but does not work yet
    while not found:
        seed = loc_to_seed(loc)
        for sr in seed_ranges:
            if seed in sr:
                print(loc)
                found = True
                break
            loc += 1
    # ugly brute force
    # locs = []
    # for i, (start, size) in enumerate(seed_ranges):
    #     locs.append((min(seed_to_loc(seed) for seed in range(start, start+size)), i))
    # # part 2 : 20191102
    # print(min(locs))


if __name__ == '__main__':
    main()

