import re

with open('input/day21.txt') as file:
    food_strings = file.read().splitlines()
foods = []
for food_string in food_strings:
    ingredients_string, allergens_string = re.search(r'(.+) \(contains (.+)\)', food_string).groups()
    ingredients_set = set(ingredients_string.split(' '))
    allergens = allergens_string.split(', ')
    foods.append((ingredients_set, allergens))
all_ingredients_set = set()
possible_ingredients_set_per_allergen = {}
count_per_ingredient = {}
for ingredients_set, allergens in foods:
    all_ingredients_set.update(ingredients_set)
    for allergen in allergens:
        possible_ingredients_set_per_allergen.setdefault(allergen, ingredients_set.copy())
        possible_ingredients_set_per_allergen[allergen] &= ingredients_set
    for ingredient in ingredients_set:
        count_per_ingredient.setdefault(ingredient, 0)
        count_per_ingredient[ingredient] += 1
safe_ingredients_set = all_ingredients_set - set.union(*possible_ingredients_set_per_allergen.values())
safe_ingredients_total_count = sum(count_per_ingredient[ingredient] for ingredient in safe_ingredients_set)
print(safe_ingredients_total_count)

ingredient_per_allergen = {}
unknown_ingredient_allergen_set = set(possible_ingredients_set_per_allergen.keys())
while unknown_ingredient_allergen_set:
    for allergen in unknown_ingredient_allergen_set:
        possible_ingredients_set_per_allergen[allergen] -= set(ingredient_per_allergen.values())
        if len(possible_ingredients_set_per_allergen[allergen]) == 1:
            ingredient_per_allergen[allergen] = list(possible_ingredients_set_per_allergen[allergen])[0]
    unknown_ingredient_allergen_set -= set(ingredient_per_allergen.keys())
print(','.join(ingredient_per_allergen[allergen] for allergen in sorted(ingredient_per_allergen.keys())))
