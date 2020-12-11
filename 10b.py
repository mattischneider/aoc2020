from operator import mul
from functools import reduce
FILE_NAME = "10.txt"

with open(FILE_NAME, 'r') as f:
    JOLTAGE_OUTPUTS = f.read().split('\n')
    JOLTAGE_OUTPUTS = [int(i) for i in JOLTAGE_OUTPUTS]
    JOLTAGE_OUTPUTS.sort()


def get_fibonacci_on_speed_array(size):
    output = [1, 2, 4]
    for i in range(3, size):
        output.append(sum(output[i-3:i]))
    return(output)


def get_three_jolt_jumps():
    output = [{'to': -3}]
    for i in JOLTAGE_OUTPUTS:
        if i + 1 not in JOLTAGE_OUTPUTS:
            output.append({'from': output[-1]['to']+3, 'to': i})
    return(output)


# second part
fib_on_speed = get_fibonacci_on_speed_array(len(JOLTAGE_OUTPUTS))
three_jolt_jumps = get_three_jolt_jumps()
len_1_step_runs = [i['to'] - i['from'] -
                   1 for i in three_jolt_jumps[1:] if i['to'] != i['from']]
mult = [fib_on_speed[i] for i in len_1_step_runs]
print(reduce(mul, mult, 1))
