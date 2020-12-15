FILE_NAME = "13.txt"

with open(FILE_NAME, 'r') as f:
    bus_data = f.read().split('\n')
    ARRIVAL_TIME = int(bus_data[0])
    X_BUS = bus_data[1].split(',')
    BUSSES = [int(b) for b in X_BUS if b != 'x']


def get_next_arrival_time(current_minute, bus):
    last_arrival_time = current_minute - current_minute % bus
    if last_arrival_time == current_minute:
        return last_arrival_time
    else:
        return last_arrival_time + bus


# first part
next_arrival_times = [get_next_arrival_time(ARRIVAL_TIME, b) for b in BUSSES]
waiting_time = min(next_arrival_times) - ARRIVAL_TIME
next_bus = BUSSES[next_arrival_times.index(min(next_arrival_times))]
print(waiting_time, next_bus, waiting_time*next_bus)

# second part -- this only works if you let ir run VERY long :(
BUSSES.sort(reverse=True)
biggest_bus = BUSSES[0]
biggest_bus_idx = 0
busses_idx = [X_BUS.index(str(b)) for b in BUSSES]
# "solution" means: t = solution * biggest_bus - biggest_bus_idx
solution = int((100000000000000 + biggest_bus_idx) / biggest_bus)
solution_correct = {}
while True:
    if (solution * biggest_bus - biggest_bus_idx) % 10000000000000 == 0:
        print(solution, solution * biggest_bus - biggest_bus_idx)
    for idx, bus in zip(busses_idx[1:], BUSSES[1:]):
        if (solution * biggest_bus - biggest_bus_idx + idx) % bus != 0:
            solution_correct[bus] = False
            solution += 1
            break
        else:
            solution_correct[bus] = True
    if all(solution_correct.values()) == True:
        break

print(solution, solution * biggest_bus - biggest_bus_idx)
