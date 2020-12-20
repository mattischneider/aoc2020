FILE_NAME = "20.txt"

with open(FILE_NAME, 'r') as f:
    tiles_raw = f.read().split('\n\n')
    tiles = {}
    for t in tiles_raw:
        tile_name, tile_def = t.split(':\n')
        tiles[int(tile_name.replace('Tile ', ''))] = tile_def.splitlines()


def get_all_possible_sides(tile_def):
    left_side = ''.join([tile_def[i][0] for i in range(len(tile_def))])
    rigth_side = ''.join([tile_def[i][-1] for i in range(len(tile_def))])
    top_side = tile_def[0]
    bottom_side = tile_def[-1]
    output = [left_side, rigth_side, top_side, bottom_side,
              left_side[::-1], rigth_side[::-1], top_side[::-1], bottom_side[::-1]]
    return output


def get_number_of_impossible_side_matches(tile_name, tiles):
    possible_sides = get_all_possible_sides(tiles[tile_name])
    all_other_sides = []
    for t in tiles.keys():
        if t != tile_name:
            all_other_sides += get_all_possible_sides(tiles[t])
    out = sum(1 for s in possible_sides if s not in all_other_sides)
    return(out)


# first part
corners = [t for t in tiles.keys(
) if get_number_of_impossible_side_matches(t, tiles) == 4]

print('part 1:', corners[0]*corners[1]*corners[2]*corners[3])
