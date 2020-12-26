class CrabCups:

    def __init__(self, cup_list, number_of_rounds):
        self.cup_list = list(cup_list)
        self.current_cup = self.cup_list[0]
        self.number_of_cups = len(self.cup_list)
        self.number_of_rounds = number_of_rounds

    def show_current_cups(self):
        return ' '.join(str(i).replace(str(self.current_cup), '('+str(self.current_cup)+')')
                        for i in self.cup_list)

    def reshuffle_cup_list(self, first_cup):
        current_cup_idx = self.cup_list.index(first_cup)
        if current_cup_idx > 0:
            self.cup_list = self.cup_list[current_cup_idx:len(
                self.cup_list)] + self.cup_list[0:current_cup_idx]
        return current_cup_idx

    def get_three_picked_up_cups(self):
        picked_up_cups = []
        for i in range(3):
            next_pop_idx = (self.cup_list.index(
                self.current_cup) + 1) % len(self.cup_list)
            picked_up_cups.append(self.cup_list.pop(next_pop_idx))
        return picked_up_cups

    def get_distination_cup(self, picked_up_cups):
        destination_cup = self.current_cup - 1
        while destination_cup in picked_up_cups or destination_cup == 0:
            destination_cup -= 1
            if destination_cup <= 0:
                destination_cup = self.number_of_cups
        dest_idx = self.cup_list.index(destination_cup)
        return destination_cup, dest_idx

    def move(self):
        picked_up_cups = self.get_three_picked_up_cups()
        destination_cup, dest_idx = self.get_distination_cup(picked_up_cups)
        self.cup_list.insert(dest_idx + 1, picked_up_cups[2])
        self.cup_list.insert(dest_idx + 1, picked_up_cups[1])
        self.cup_list.insert(dest_idx + 1, picked_up_cups[0])
        self.current_cup = self.cup_list[(self.cup_list.index(self.current_cup) + 1) %
                                         self.number_of_cups]
        return destination_cup, picked_up_cups

    def play(self, part=1):
        for i in range(self.number_of_rounds):
            self.move()
        if part == 1:
            return self.get_final_list()
        if part == 2:
            return self.get_final_product()

    def get_final_list(self):
        self.reshuffle_cup_list(1)
        return self.cup_list[1:len(self.cup_list)]

    def get_final_product(self):
        self.reshuffle_cup_list(1)
        return self.cup_list[1] * self.cup_list[2]


INPUT = '963275481'
# first part
cc = CrabCups(cup_list=[int(i) for i in INPUT], number_of_rounds=100)
print('First Part: ' + ''.join(map(str, cc.play(part=1))))

# second part
# cc = CrabCups(cup_list=[int(i) for i in INPUT] +
#              list(range(10, 1_000_001)), number_of_rounds=10_000_000)
# print('#####\nSecond Part:', cc.play(part=2))
