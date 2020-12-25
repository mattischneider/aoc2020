import re


class TileFloor:
    def __init__(self):
        self.black_tiles = []

    def flip(self, instruction):
        instruction_steps = [i for i in re.split(
            r'(ne|se|sw|nw|w|e)', instruction) if i != '']
        instruction_steps = [i.replace('ne', '1, 2').replace(
            'se', '-1, 2').replace('sw', '-1, -2').replace('nw', '1, -2').replace('w', '0, -4').replace('e', '0, 4') for i in instruction_steps]
        instruction_steps = [list(map(int, i.split(', ')))
                             for i in instruction_steps]
        position = [sum(i[0] for i in instruction_steps), sum(i[1]
                                                              for i in instruction_steps)]
        if position not in self.black_tiles:
            self.black_tiles.append(position)
        else:
            self.black_tiles.remove(position)

    def get_all_adjacent_tiles(self, position):
        x = position[0]
        y = position[1]
        neighbours = [[1, 2], [-1, 2], [-1, -2], [1, -2], [0, -4], [0, 4]]
        return([[x+dx, y+dy] for dx, dy in neighbours])

    def get_number_of_adjacent_black_tiles(self, position):
        return(sum(1 for n in self.get_all_adjacent_tiles(position) if n in self.black_tiles))

    def next_day(self):
        tiles_that_stay_black = [
            p for p in self.black_tiles if self.get_number_of_adjacent_black_tiles(p) in (1, 2)]
        whites_adjacent_to_blacks = []
        for b in self.black_tiles:
            for n in self.get_all_adjacent_tiles(b):
                if n not in self.black_tiles and n not in whites_adjacent_to_blacks:
                    whites_adjacent_to_blacks.append(n)
        flip_to_black = [
            w for w in whites_adjacent_to_blacks if self.get_number_of_adjacent_black_tiles(w) == 2]
        self.black_tiles = tiles_that_stay_black + flip_to_black

    def get_number_of_black_tiles(self):
        return len(self.black_tiles)


FILE_NAME = "24.txt"
with open(FILE_NAME, 'r') as f:
    flip_instructions = f.read().splitlines()

t = TileFloor()

# first part
for i in flip_instructions:
    t.flip(i)

print('first part:', t.get_number_of_black_tiles())

# second part
for day in range(100):
    t.next_day()

print('Day', day+1, ':', t.get_number_of_black_tiles())
