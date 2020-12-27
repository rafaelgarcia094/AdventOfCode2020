child_bags = {}

for _ in range(594):
    outer_bag, inner_bags = input().split(' contain ')
    inner_bags = inner_bags[:-1].split(', ')

    if inner_bags[0] == 'no other bags':
        continue

    child_bags[outer_bag] = []

    for bag in inner_bags:
        amount = int(bag[0])
        name = bag[2:] + ('s' * (amount == 1))

        child_bags[outer_bag].append((name, amount))

my_bags = [('shiny gold bags', 1)]
n_bags = 0

while my_bags:
    my_bag, amount = my_bags[0]
    my_bags = my_bags[1:]

    if my_bag not in child_bags:
        continue

    for child_bag, child_amount in child_bags[my_bag]:
        actual_amount = amount * child_amount
        n_bags += actual_amount
        my_bags.append((child_bag, actual_amount))

print(n_bags)
