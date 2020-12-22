class Combat:

    def __init__(self, player_1_cards, player_2_cards):
        self.game_history = []
        self.player_1_cards = list(player_1_cards)
        self.player_2_cards = list(player_2_cards)

    def get_winner_and_winning_score(self):
        final_deck = self.player_1_cards + self.player_2_cards
        if len(self.player_1_cards) == 0:
            winner = 2
        if len(self.player_2_cards) == 0:
            winner = 1
        winning_score = sum((len(final_deck) - idx) * card for idx,
                            card in enumerate(final_deck))
        return winner, winning_score

    def next_round(self):
        p1_top_card = self.player_1_cards.pop(0)
        p2_top_card = self.player_2_cards.pop(0)
        if p1_top_card > p2_top_card:
            self.player_1_cards.append(p1_top_card)
            self.player_1_cards.append(p2_top_card)
        if p2_top_card > p1_top_card:
            self.player_2_cards.append(p2_top_card)
            self.player_2_cards.append(p1_top_card)

    def play_normal(self):
        while len(self.player_1_cards) > 0 and len(self.player_2_cards) > 0:
            self.next_round()
        return(self.get_winner_and_winning_score())

    def next_recursive_round(self):
        if [self.player_1_cards, self.player_2_cards] in self.game_history:  # to avoid infinite games
            game_winner = 1
            winning_score = 0  # score does not matter in sub-games
            self.player_2_cards = []
            return game_winner, winning_score
        else:
            self.game_history.append(
                [list(self.player_1_cards), list(self.player_2_cards)])
        p1_top_card = self.player_1_cards.pop(0)
        p2_top_card = self.player_2_cards.pop(0)
        if p1_top_card <= len(self.player_1_cards) and p2_top_card <= len(self.player_2_cards):
            rec_game = Combat(
                self.player_1_cards[0:p1_top_card], self.player_2_cards[0:p2_top_card])
            round_winner, subgame_score = rec_game.play_recursive()
        else:
            if p1_top_card > p2_top_card:
                round_winner = 1
            if p2_top_card > p1_top_card:
                round_winner = 2
        if round_winner == 1:
            self.player_1_cards.append(p1_top_card)
            self.player_1_cards.append(p2_top_card)
        if round_winner == 2:
            self.player_2_cards.append(p2_top_card)
            self.player_2_cards.append(p1_top_card)

    def play_recursive(self):
        while len(self.player_1_cards) > 0 and len(self.player_2_cards) > 0:
            self.next_recursive_round()
        return(self.get_winner_and_winning_score())


FILE_NAME = "22.txt"

with open(FILE_NAME, 'r') as f:
    p1, p2 = f.read().split('\n\n')
    p1 = p1.splitlines()
    p1_start_cards = [int(i) for i in p1[1:]]
    p2 = p2.splitlines()
    p2_start_cards = [int(i) for i in p2[1:]]


# part1
c_normal = Combat(p1_start_cards, p2_start_cards)
print(c_normal.play_normal())

# part2
#recursive_test = Combat([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
# print(recursive_test.play_recursive())

c_recursive = Combat(p1_start_cards, p2_start_cards)
print(c_recursive.play_recursive())
