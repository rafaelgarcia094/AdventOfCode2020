def calculate_loop_size(public_key, number):
    loop_size = 0
    temp_number = 1

    while temp_number != public_key:
        temp_number *= number
        temp_number = temp_number % 20201227
        loop_size += 1

    return loop_size


def encrypt_key(number, loop_size):
    temp_number = 1

    for i in range(loop_size):
        temp_number *= number
        temp_number = temp_number % 20201227

    return temp_number


card_public_key = int(input())
door_public_key = int(input())

subject_number = 7

card_loop_size = calculate_loop_size(card_public_key, subject_number)
door_loop_size = calculate_loop_size(door_public_key, subject_number)

print(encrypt_key(card_public_key, door_loop_size))
print(encrypt_key(door_public_key, card_loop_size))
