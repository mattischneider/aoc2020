FILE_NAME = "08.txt"

with open(FILE_NAME, 'r') as f:
    INSTRUCTIONS = f.read().split('\n')
    INSTRUCTIONS = [i.split(' ') for i in INSTRUCTIONS]


def get_next_instruction_position(current_instruction_position, instructions):
    i = instructions[current_instruction_position]
    if i[0] in ('nop', 'acc'):
        next_position = current_instruction_position + 1
    if i[0] == 'jmp':
        next_position = current_instruction_position + int(i[1])
    if next_position == len(instructions):
        return(None)  # that means termination!
    else:
        return(next_position)


def get_final_acc(instructions):
    instruction_steps = [0]  # starting point is the first instruction
    current_acc = 0
    while get_next_instruction_position(instruction_steps[-1], instructions) not in instruction_steps:
        current_instruction = instructions[instruction_steps[-1]]
        if current_instruction[0] == 'acc':
            current_acc += int(current_instruction[1])
        n = get_next_instruction_position(instruction_steps[-1], instructions)
        if n is None:
            return({'current_acc': current_acc, 'terminates': True})
        else:
            instruction_steps.append(n)
        #
    return({'current_acc': current_acc, 'terminates': False})


# first part
print(get_final_acc(INSTRUCTIONS))

# second part
for i in range(1, len(INSTRUCTIONS)):
    swaps = {'nop': 'jmp', 'jmp': 'nop'}
    if INSTRUCTIONS[i][0] in swaps:
        swap_from = INSTRUCTIONS[i][0]
        swap_to = swaps[INSTRUCTIONS[i][0]]
        INSTRUCTIONS[i][0] = swap_to
        acc = get_final_acc(INSTRUCTIONS)
        if acc['terminates'] is True:
            current_acc = acc['current_acc']
            print(
                f'swapping {swap_from} to {swap_to} in position {i} terminates the machine with acc: {current_acc}')
        INSTRUCTIONS[i][0] = swap_from
