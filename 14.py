import re

FILE_NAME = "14.txt"

with open(FILE_NAME, 'r') as f:
    PROGRAMM_INSTRUCTIONS = f.read().split('\n')


def get_unmasked_value(mask, value):
    value = value.zfill(len(mask))
    output = ''
    for idx, m in enumerate(mask):
        if m == 'X':
            output += value[idx]
        if m in ('0', '1'):
            output += m
    return output


def get_all_floating_memory_addresses(mask, addr):
    addr = addr.zfill(len(mask))
    output = []
    num_of_x_in_mask = len([c for c in mask if c == 'X'])
    for i in range(0, 2 ** num_of_x_in_mask):
        r = format(i, "b").zfill(num_of_x_in_mask)
        replaced_addr = ''
        for idx, m in enumerate(mask):
            if m == '0':
                replaced_addr += addr[idx]
            if m == '1':
                replaced_addr += '1'
            if m == 'X':
                replaced_addr += r[0]
                r = r[1:]
        output.append(replaced_addr)
    return output


def run_instructions(instructions, version=1):
    current_mask = None
    current_memory = {}
    for i in instructions:
        if i[0:4] == 'mask':
            current_mask = i[7:]
        if i[0:3] == 'mem':
            tmp = re.match('mem\[(\d*)\] = (\d*)', i)
            if version == 1:
                addr = tmp.group(1)
                value = get_unmasked_value(
                    current_mask, format(int(tmp.group(2)), "b"))
                current_memory[addr] = int(value, 2)
            if version == 2:
                value = tmp.group(2)
                addresses = get_all_floating_memory_addresses(
                    current_mask, format(int(tmp.group(1)), "b"))
                for a in addresses:
                    current_memory[int(a, 2)] = int(value)
    return current_memory


# first part
m = run_instructions(PROGRAMM_INSTRUCTIONS, version=1)
print('########')
print('PART 1')
print(sum(m.values()))

# second part
m = run_instructions(PROGRAMM_INSTRUCTIONS, version=2)
print('########')
print('PART 2')
print(sum(m.values()))
