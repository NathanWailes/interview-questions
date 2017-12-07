
number_of_cells = 4

number_of_possible_blobs = 0

for i in reversed(range(number_of_cells)):
    number_of_possible_blobs += i

print(number_of_possible_blobs)