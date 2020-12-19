import itertools

FILE_NAME = "17.txt"

with open(FILE_NAME, 'r') as f:
    initial_state = f.read().split('\n')
    initial_state = [[j for j in i] for i in initial_state]
    initial_active_cubes = []
    for idx, x in enumerate(initial_state):
        for idy, y in enumerate(x):
            if y == '#':
                initial_active_cubes.append([idx, idy])


class ConwayCube:
    def __init__(self, active_cubes, number_of_dimensions):
        self.number_of_dimensions = number_of_dimensions
        self.active_cubes = []
        for ac in active_cubes:
            for i in range(number_of_dimensions-len(ac)):
                ac.append(0)
            self.active_cubes.append(ac)

    def get_number_of_active_cubes(self):
        return(len(self.active_cubes))

    def get_next_spreading(self, dimension):
        current_spread = [active_cube[dimension]
                          for active_cube in self.active_cubes]
        return(list(range(min(current_spread)-1, max(current_spread)+2)))

    def get_all_neighbours(self, v):
        neighbours = []
        for i in range(0, 3 ** len(v)):
            nums = []
            n = 0 + i
            while n > 0:
                n, r = divmod(n, 3)
                nums.append(r-1)
            nums.reverse()
            for j in range(self.number_of_dimensions - len(nums)):
                nums = [-1] + nums
            a = [nums[idx] + v[idx]
                 for idx in range(self.number_of_dimensions)]
            neighbours.append(a)
        neighbours.remove(v)
        return(neighbours)

    def get_new_status(self, v):
        neighbours = self.get_all_neighbours(v)
        number_of_active_neighbour_cubes = sum(
            [1 for n in neighbours if n in self.active_cubes])
        if v in self.active_cubes and number_of_active_neighbour_cubes in (2, 3):
            return('active')
        if v not in self.active_cubes and number_of_active_neighbour_cubes == 3:
            return('active')
        return('inactive')

    def update_cycle(self):
        spreads = {}
        for d in range(self.number_of_dimensions):
            spreads[d] = self.get_next_spreading(d)
        new_active_cubes = []
        for p in itertools.product(*[spreads[d] for d in range(self.number_of_dimensions)]):
            v = [i for i in p]
            if self.get_new_status(v) == 'active':
                new_active_cubes.append(v)
        self.active_cubes = new_active_cubes


# first part
print('first part!')
cc = ConwayCube(initial_active_cubes, number_of_dimensions=3)
print(0, cc.get_number_of_active_cubes())
for i in range(6):
    cc.update_cycle()
    print(i+1, cc.get_number_of_active_cubes())

# second part
print('second part!')
cc = ConwayCube(initial_active_cubes, number_of_dimensions=4)
print(0, cc.get_number_of_active_cubes())
for i in range(6):
    cc.update_cycle()
    print(i+1, cc.get_number_of_active_cubes())
