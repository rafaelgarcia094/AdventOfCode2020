parent_bags = {}

for _ in range(594):
    outer_bag, inner_bags = input().split(' contain ')
    inner_bags = inner_bags[:-1].split(', ')

    if inner_bags[0] == 'no other bags':
        continue

    for bag in inner_bags:
        amount = int(bag[0])
        name = bag[2:] + ('s' * (amount == 1))

        if name not in parent_bags:
            parent_bags[name] = [outer_bag]
        else:
            parent_bags[name].append(outer_bag)

my_bags = ['shiny gold bags']
checked_bags = set(my_bags)
n_bags = 0

while my_bags:
    my_bag = my_bags[0]
    my_bags = my_bags[1:]

    if my_bag not in parent_bags:
        continue

    for parent_bag in parent_bags[my_bag]:
        if parent_bag not in checked_bags:
            checked_bags.add(parent_bag)
            my_bags.append(parent_bag)
            n_bags += 1

print(n_bags)
