import re
from operator import mul
from functools import reduce

FILE = "16.txt"


def get_input_variables(filename):
    with open(filename, 'r') as f:
        txt_input = f.read().split('\n\n')
        restrictions = txt_input[0].split('\n')
        restrictions_out = {}
        for r in restrictions:
            tmp = r.split(':')
            name = tmp[0]
            tmp2 = tmp[1].split(' or ')
            first_conditional = tmp2[0]
            second_conditional = tmp2[1]
            restrictions_out[name] = {
                'first_conditional': first_conditional, 'second_conditional': second_conditional}
        my_ticket = txt_input[1].split('\n')
        my_ticket = [int(i) for i in my_ticket[1].split(',')]
        nearby_tickets = txt_input[2].split('\n')
        nearby_tickets = [[int(j) for j in i.split(',')]
                          for i in nearby_tickets[1:]]
    return(restrictions_out, my_ticket, nearby_tickets)


def is_ticket_value_in_range(ticket_value, bounds_range):
    bounds = bounds_range.split('-')
    return(int(bounds[0]) <= ticket_value <= int(bounds[1]))


def is_in_restriction_range(restriction, ticket_value):
    in_any_range = any([is_ticket_value_in_range(
        ticket_value=ticket_value, bounds_range=restriction[cond]) for cond in restriction])
    return(in_any_range)


def get_invalid_ticket_value(ticket, restrictions):
    for ticket_value in ticket:
        if not any([is_in_restriction_range(restriction=restrictions[r], ticket_value=ticket_value) for r in restrictions]):
            return ({'is_valid_ticket': False, 'invalid_ticket_value': ticket_value})
    return ({'is_valid_ticket': True})


def get_position_of_restriction_name(restriction, all_valid_tickets):
    valid_positions = []
    for i in range(0, len(all_valid_tickets[0])):
        ticket_values_at_position_i = [t[i] for t in all_valid_tickets]
        if all([is_in_restriction_range(restriction=restriction, ticket_value=ticket_value) for ticket_value in ticket_values_at_position_i]):
            valid_positions.append(i)
    return valid_positions


# first part
restrictions, my_ticket, nearby_tickets = get_input_variables(FILE)
invalid_ticket_values = [get_invalid_ticket_value(
    nt, restrictions) for nt in nearby_tickets]
print(sum(i['invalid_ticket_value']
          for i in invalid_ticket_values if i['is_valid_ticket'] is False))

# second part
valid_tickets = [
    t for t in nearby_tickets if get_invalid_ticket_value(t, restrictions)['is_valid_ticket'] is True]
valid_tickets.append(my_ticket)

for r in restrictions:
    restrictions[r]['valid_positions'] = get_position_of_restriction_name(
        restriction=restrictions[r], all_valid_tickets=valid_tickets)


def remove_from_valid_positions(pos):
    for r in restrictions:
        valid_pos = restrictions[r]['valid_positions']
        if len(valid_pos) > 1 and pos in valid_pos:
            restrictions[r]['valid_positions'].remove(pos)


while True:
    for r in restrictions:
        valid_positions = restrictions[r]['valid_positions']
        if len(valid_positions) == 1:
            position = valid_positions[0]
            remove_from_valid_positions(position)
            continue
    res_pos = [len(restrictions[r]['valid_positions'])
               == 1 for r in restrictions]
    if all(res_pos):
        break

departure_values = []
for r in restrictions:
    res_pos = restrictions[r]['valid_positions'][0]
    if 'departure' in r:
        departure_values.append(my_ticket[res_pos])

print(reduce(mul, departure_values, 1))
