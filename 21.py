FILE_NAME = "21.txt"

with open(FILE_NAME, 'r') as f:
    foods = f.read().splitlines()
    foods = [i.split(' (contains ') for i in foods]
    foods = [[f[0].split(' '), f[1].replace(')', '').split(', ')]
             for f in foods]

all_allergens = set(t for f in foods for t in f[1])
all_ingredients = set(t for f in foods for t in f[0])
possible_translations = {}

for current_ingredients, current_allergens in foods:
    for a in current_allergens:
        if a in possible_translations.keys():
            possible_translations[a] = [
                t for t in current_ingredients if t in possible_translations[a]]
        else:
            possible_translations[a] = current_ingredients

while any(len(possible_translations[allergen]) > 1 for allergen in possible_translations):
    for a in possible_translations:
        if len(possible_translations[a]) == 1:
            final_solution = possible_translations[a][0]
            for b in possible_translations:
                if b != a and final_solution in possible_translations[b]:
                    possible_translations[b].remove(final_solution)

known_allergen_translations = [t[0] for t in possible_translations.values()]

# part 1
print(sum(1 for f in foods for t in f[0]
          if t not in known_allergen_translations))

# part 2
a_names = list(possible_translations.keys())
a_names.sort()
print(','.join(possible_translations[a][0] for a in a_names))
