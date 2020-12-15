INPUT = '5, 2, 8, 16, 18, 0, 1'
INPUT_SEQUENCE = [int(i) for i in INPUT.split(', ')]


def get_spoken_number(start_sequence, stop_after):
    current_idx = len(start_sequence) + 1
    last_number_spoken = start_sequence[-1]
    last_two_occurences = {}
    for idx, i in enumerate(start_sequence):
        last_two_occurences[i] = [idx + 1]
    while current_idx <= stop_after:
        # get next number spoken
        if last_number_spoken not in last_two_occurences or len(last_two_occurences[last_number_spoken]) < 2:
            next_number_spoken = 0
        else:
            last_occurence = max(last_two_occurences[last_number_spoken])
            last_last_occurence = min(last_two_occurences[last_number_spoken])
            next_number_spoken = last_occurence - last_last_occurence
        # update the array in last_two_occurences
        if next_number_spoken not in last_two_occurences:
            last_two_occurences[next_number_spoken] = [current_idx]
        else:
            m = max(last_two_occurences[next_number_spoken])
            last_two_occurences[next_number_spoken] = [m, current_idx]
        # next step
        last_number_spoken = next_number_spoken
        current_idx += 1
    return(last_number_spoken)


# first part
print(get_spoken_number(INPUT_SEQUENCE, stop_after=2020))

# second part
print(get_spoken_number(INPUT_SEQUENCE, stop_after=30000000))
