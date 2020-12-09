FILE_NAME = "09.txt"

with open(FILE_NAME, 'r') as f:
    TEH_NUMBERS = f.read().split('\n')
    TEH_NUMBERS = [int(i) for i in TEH_NUMBERS]


def is_sum_of_two_of_the_previous_25_numbers(line_idx):
    current_number = TEH_NUMBERS[line_idx-1]
    base_numbers = TEH_NUMBERS[line_idx-26:line_idx-1]
    all_possible_numbers = [
        int(x)+int(y) for x in base_numbers for y in base_numbers if x != y]
    if current_number in all_possible_numbers:
        return({'is_sum': True})
    else:
        return({'is_sum': False, 'invalid_number': current_number})


# first part:
for i in range(26, len(TEH_NUMBERS)):
    tmp = is_sum_of_two_of_the_previous_25_numbers(i)
    if tmp['is_sum'] is False:
        invalid_number = tmp['invalid_number']
        break

print(invalid_number)

# second part:


def get_first_contiguous_set(line_idx):
    for start in range(0, line_idx-1):
        for end in range(start, line_idx):
            if sum(TEH_NUMBERS[start+1:end]) == invalid_number:
                return(TEH_NUMBERS[start:end])


a = get_first_contiguous_set(TEH_NUMBERS.index(invalid_number))
print(min(a) + max(a))
