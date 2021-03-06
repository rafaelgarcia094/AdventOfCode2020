allergen_to_food = {}
allergic_food = set()


def set_allergic_food(substance):
    bad_food = list(allergen_to_food.get(substance))[0]

    for subs in allergen_to_food.keys():
        if subs != substance and bad_food in allergen_to_food[subs]:
            allergen_to_food[subs].remove(bad_food)

            if len(allergen_to_food[subs]) == 1:
                set_allergic_food(subs)

    allergic_food.add(bad_food)


for _ in range(45):
    line = input()[:-1]
    food_str, allergen_str = line.split(' (contains ')
    food_list = food_str.split(' ')
    allergen_list = allergen_str.split(', ')

    for allergen in allergen_list:
        if allergen not in allergen_to_food:
            allergen_to_food[allergen] = set(food_list).difference(allergic_food)
        elif len(allergen_to_food[allergen]) == 1:
            continue
        else:
            allergen_to_food[allergen] = allergen_to_food.get(allergen).intersection(set(food_list))

        if len(allergen_to_food[allergen]) == 1:
            set_allergic_food(allergen)

dangerous_ingredients = ''
for allergen in sorted(allergen_to_food.keys()):
    name = allergen_to_food[allergen].pop()
    dangerous_ingredients = dangerous_ingredients + name + ','

print(dangerous_ingredients[:-1])
