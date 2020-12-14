import copy
FILE_NAME = "11.txt"

with open(FILE_NAME, 'r') as f:
    SEATINGPLAN_START = f.read().split('\n')
    SEATINGPLAN_START = [[i for i in p] for p in SEATINGPLAN_START]


def get_number_of_visible_seats(i, j, seatingplan, looking_distance):
    ranges = [-1, 0, 1]
    num_of_cols = len(seatingplan)
    num_of_rows = len(seatingplan[0])
    number_of_visible_seats = 0
    for k in ranges:
        for l in ranges:
            if (k, l) != (0, 0):
                for current_looking_distance in range(1, looking_distance+1):
                    look_at_i = i + k * current_looking_distance
                    look_at_j = j + l * current_looking_distance
                    if 0 <= look_at_i < num_of_cols and 0 <= look_at_j < num_of_rows:
                        look_at_seat = seatingplan[look_at_i][look_at_j]
                        if look_at_seat == '#':
                            number_of_visible_seats += 1
                            break
                        if look_at_seat == 'L':
                            break
                        if look_at_seat == '.':
                            continue
    return(number_of_visible_seats)


def update_seatingplan_position(i, j, seatingplan, max_treshhold, looking_distance):
    new_occupancy_status = copy.deepcopy(seatingplan[i][j])
    num_of_vis_seats = get_number_of_visible_seats(
        i, j, seatingplan, looking_distance)
    if num_of_vis_seats == 0 and seatingplan[i][j] == 'L':
        new_occupancy_status = '#'
    if num_of_vis_seats >= max_treshhold and seatingplan[i][j] == '#':
        new_occupancy_status = 'L'
    return(new_occupancy_status)


def update_seatingplan(seatingplan, max_treshhold, looking_distance):
    number_of_changes = 0
    new_seatingplan = copy.deepcopy(seatingplan)
    for i in range(0, len(seatingplan)):
        for j in range(0, len(seatingplan[0])):
            if seatingplan[i][j] != '.':
                new_occupancy_status = update_seatingplan_position(
                    i, j, seatingplan, max_treshhold, looking_distance)
                if new_seatingplan[i][j] != new_occupancy_status:
                    new_seatingplan[i][j] = new_occupancy_status
                    number_of_changes += 1
    return(number_of_changes, new_seatingplan)


def get_number_of_occupied_seats(seatingplan):
    return(sum([1 for j in seatingplan for i in j if i == '#']))


def passengers_finding_seats(seatingplan, max_treshhold, looking_distance):
    step_number = 0
    more_steps_needed = True
    while more_steps_needed == True:
        step_number += 1
        new_seatingplan = copy.deepcopy(seatingplan)
        number_of_changes, new_seatingplan = update_seatingplan(
            seatingplan, max_treshhold, looking_distance)
        seatingplan = copy.deepcopy(new_seatingplan)
        if number_of_changes == 0:
            more_steps_needed = False
    occupied_seats = get_number_of_occupied_seats(seatingplan)
    return({'steps_needed': step_number-1, 'occupied_seats': occupied_seats})


# part 1:
print(passengers_finding_seats(SEATINGPLAN_START,
                               max_treshhold=4, looking_distance=1))

# part 2:
print(passengers_finding_seats(SEATINGPLAN_START,
                               max_treshhold=5, looking_distance=len(SEATINGPLAN_START)))
