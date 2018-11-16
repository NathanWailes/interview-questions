


number_of_digits = 0

current_number = 0

while number_of_digits < 2040:
    current_number += 1
    current_number_number_of_digits = len('%d' % current_number)

    number_of_digits += current_number_number_of_digits

print(current_number)