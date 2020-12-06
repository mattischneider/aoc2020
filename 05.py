FILE = "05.txt"

with open(FILE, 'r') as f:
    tickets = f.read().split('\n')


def get_row_number(ticket):
    return(int(ticket[0:7].replace('F', '0').replace('B', '1'), 2))


def get_column_number(ticket):
    return(int(ticket[7:10].replace('L', '0').replace('R', '1'), 2))


def get_seat_id(ticket):
    return(get_row_number(ticket) * 8 + get_column_number(ticket))


seat_ids = [get_seat_id(t) for t in tickets]

# first part
print(max(seat_ids))

# second part
print(set(range(min(seat_ids), max(seat_ids)+1)).symmetric_difference(seat_ids))
