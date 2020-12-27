order = input()

for _ in range(100):
    picked = order[1:4]
    order = order[4:] + order[:1]

    destination = 9 if (r := int(order[-1]) - 1) == 0 else r
    while str(destination) in picked:
        destination = 9 if (r := destination - 1) == 0 else r

    destination_idx = order.find(str(destination))

    order = order[:destination_idx+1] + picked + order[destination_idx+1:]

idx_one_pos = order.find('1')
final_order = order[idx_one_pos+1:] + order[:idx_one_pos]
print(final_order)
