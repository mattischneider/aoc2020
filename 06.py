FILE = "06.txt"

with open(FILE, 'r') as f:
    group_answers = f.read().split('\n\n')
    group_answers = [p.replace('\n', ' ').split(' ') for p in group_answers]

# first part
print(sum([len(set(''.join(a))) for a in group_answers]))

# second part
print(sum([len(set.intersection(*[set(i) for i in a]))
           for a in group_answers]))
