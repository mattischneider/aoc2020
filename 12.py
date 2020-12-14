FILE_NAME = "12.txt"

with open(FILE_NAME, 'r') as f:
    INSTRUCTIONS = f.read().split('\n')
    INSTRUCTIONS = [
        {'action': i[0], 'value': int(i[1:])} for i in INSTRUCTIONS]


def get_facing_direction_on_grid(facing_degree):
    if facing_degree == 0:
        return([1, 0])
    if facing_degree == 90:
        return([0, 1])
    if facing_degree == 180:
        return([-1, 0])
    if facing_degree == 270:
        return([0, -1])


# first part
POSITION = [0, 0]  # east, north grid
FACING_DEGREE = 0  # 0 - east, ..
FACING_DIRECTION = get_facing_direction_on_grid(FACING_DEGREE)
for i in INSTRUCTIONS:
    if i['action'] == 'N':
        POSITION[1] += i['value']
    if i['action'] == 'S':
        POSITION[1] -= i['value']
    if i['action'] == 'E':
        POSITION[0] += i['value']
    if i['action'] == 'W':
        POSITION[0] -= i['value']
    if i['action'] == 'L':
        FACING_DEGREE = (FACING_DEGREE + i['value']) % 360
        FACING_DIRECTION = get_facing_direction_on_grid(FACING_DEGREE)
    if i['action'] == 'R':
        FACING_DEGREE = (FACING_DEGREE - i['value']) % 360
        FACING_DIRECTION = get_facing_direction_on_grid(FACING_DEGREE)
    if i['action'] == 'F':
        tmp = [f * i['value'] for f in FACING_DIRECTION]
        POSITION[0] += tmp[0]
        POSITION[1] += tmp[1]

print('########')
print('PART 1')
print('final ship position: ' + str(POSITION))
print('manhattan distance: ' + str(sum(map(abs, POSITION))))


def get_new_waypoint_position(waypoint_position, turning_degree, turning_direction):
    new_x, new_y = waypoint_position[0], waypoint_position[1]
    for i in range(0, int(turning_degree/90)):
        if turning_direction == 'R':
            new_x, new_y = new_y, -new_x
        if turning_direction == 'L':
            new_x, new_y = -new_y, new_x
    return([new_x, new_y])


# second part
SHIP_POSITION = [0, 0]  # east, north grid
WAYPOINT_POSITION = [10, 1]  # east, north grid
for i in INSTRUCTIONS:
    if i['action'] == 'N':
        WAYPOINT_POSITION[1] += i['value']
    if i['action'] == 'S':
        WAYPOINT_POSITION[1] -= i['value']
    if i['action'] == 'E':
        WAYPOINT_POSITION[0] += i['value']
    if i['action'] == 'W':
        WAYPOINT_POSITION[0] -= i['value']
    if i['action'] in ('L', 'R'):
        WAYPOINT_POSITION = get_new_waypoint_position(
            WAYPOINT_POSITION, i['value'], i['action'])
    if i['action'] == 'F':
        tmp = [f * i['value'] for f in WAYPOINT_POSITION]
        SHIP_POSITION[0] += tmp[0]
        SHIP_POSITION[1] += tmp[1]

print('########')
print('PART 2')
print('final ship position: ' + str(SHIP_POSITION))
print('manhattan distance: ' + str(sum(map(abs, SHIP_POSITION))))
