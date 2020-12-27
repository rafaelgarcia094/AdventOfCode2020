class CupNode:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node


class CupCircle:
    def __init__(self, initial_order):
        self.first_cup = CupNode(initial_order[0])
        self.pointers = {initial_order[0]: self.first_cup}

        last_node = self.first_cup
        for v in initial_order[1:]:
            cup = CupNode(v)
            self.pointers[v] = cup

            last_node.right = cup
            cup.left = last_node

            last_node = cup

        last_node.right = self.first_cup
        self.first_cup.left = last_node

    def pick(self):
        first_cup_value = self.first_cup.value()

        cup = self.first_cup
        picked_values = []
        picked_pointers = []
        for _ in range(3):
            cup = cup.right
            picked_values.append(cup.value())
            picked_pointers.append(cup)

        destination = 1000000 if (r := first_cup_value - 1) == 0 else r
        while destination in picked_values:
            destination = 1000000 if (r := destination - 1) == 0 else r

        destination_pointer = self.pointers.get(destination)

        after_destination_pointer = destination_pointer.right
        after_picked_pointer = picked_pointers[2].right

        destination_pointer.right = picked_pointers[0]
        after_destination_pointer.left = picked_pointers[2]
        picked_pointers[0].left = destination_pointer
        picked_pointers[2].right = after_destination_pointer
        self.first_cup.right = after_picked_pointer
        after_picked_pointer.left = self.first_cup

        self.first_cup = self.first_cup.right

    def cups_with_stars(self):
        cup_one = self.pointers[1]
        return cup_one.right.value() * cup_one.right.right.value()


order = list(map(int, list(input()))) + [i for i in range(10, 1000001)]

circle = CupCircle(order)

for _ in range(10000000):
    circle.pick()

result = circle.cups_with_stars()

print(result)
