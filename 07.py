import re

FILE = "07.txt"
GOLD = 'shiny gold'
BAGS_DEFS = {}
BAGS_CHILD_COUNT = {}

with open(FILE, 'r') as f:
    BAGS = f.read().split('\n')
    for idx, bag in enumerate(BAGS):
        s = bag.split(' bags contain', 1)
        tmp = re.sub('(bags|bag|\.)', '', s[1]).split(',')
        contained_in_bag = []
        if tmp == [' no other ']:
            contained_in_bag = None
            bag_children = None
            bag_counts = None
        else:
            for t in tmp:
                a = t.strip().split(' ', 1)
                contained_in_bag.append({a[1]: a[0]})
            bag_children = [list(b.keys())[0] for b in contained_in_bag]
            bag_counts = [list(b.values())[0] for b in contained_in_bag]
        BAGS_DEFS[s[0]] = bag_children
        BAGS_CHILD_COUNT[s[0]] = bag_counts


ALL_BAGS = list(BAGS_DEFS.keys())

# first part


def any_leaf_contains_gold(bag_name):
    if BAGS_DEFS[bag_name] is None:
        return(False)
    if GOLD in BAGS_DEFS[bag_name]:
        return(True)
    return(any(any_leaf_contains_gold(b) for b in BAGS_DEFS[bag_name]))


print(len(set([b for b in ALL_BAGS if any_leaf_contains_gold(b) is True])))


# second part

def get_number_of_bags_inside(bag_name):
    if BAGS_DEFS[bag_name] is None:
        return(0)
    else:
        children_names = BAGS_DEFS[bag_name]
        children_counts = BAGS_CHILD_COUNT[bag_name]
        l = len(children_names)
        return(sum([int(children_counts[i]) + int(children_counts[i]) * get_number_of_bags_inside(children_names[i]) for i in range(0, l)]))


print(get_number_of_bags_inside(GOLD))
