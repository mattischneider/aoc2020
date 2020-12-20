import re

FILE_NAME = "18.txt"

with open(FILE_NAME, 'r') as f:
    expressions = f.read().splitlines()


class AlienExpression(int):

    def __add__(self, y):
        return AlienExpression(int(self)+y)

    def __sub__(self, y):
        return AlienExpression(int(self)*y)


def get_alien_expression(expression):
    new_exp = re.sub(r'(\d+)', r'AlienExpression(\1)', expression)
    new_exp = new_exp.replace('*', '-')
    return new_exp


# part 1
print(sum([eval(get_alien_expression(exp)) for exp in expressions]))


class AlienExpression_p2(int):

    def __mul__(self, y):
        return AlienExpression_p2(int(self)+y)

    def __sub__(self, y):
        return AlienExpression_p2(int(self)*y)


def get_alien_expression_p2(expression):
    new_exp = re.sub(r'(\d+)', r'AlienExpression_p2(\1)', expression)
    new_exp = new_exp.replace('*', '-').replace('+', '*')
    return new_exp


# part 2:
print(sum([eval(get_alien_expression_p2(exp)) for exp in expressions]))
