timestamp = int(input())
buses = list(map(int, filter(lambda c: c != 'x', input().split(','))))
minutes_to_wait = [bus_id - (timestamp % bus_id) for bus_id in buses]
chosen_bus = min(zip(minutes_to_wait, buses))
result = chosen_bus[0] * chosen_bus[1]
print(result)
