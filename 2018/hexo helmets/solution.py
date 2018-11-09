# list = [4, 2, 1, 3, 10, 7, 8]

# We know the list is somewhat sorted.
# Each element is at most 3 positions away 
# from where it should be.

k = 2
list = [1, 2]
list = [2, 1]

# For k=2, n=2:
# Save a reference to the current position.
# Look at the next position.
# If the element in the next position is greater
# than the element in the 'current' position, you
# know the first element is in the right spot.
# Otherwise, you need to swap them.

k = 2
list = [1, 2, 3]
list = [1, 3, 2]
list = [2, 1, 3]
list = [2, 3, 1] # [1, 3, 2]
list = [3, 1, 2]
list = [3, 2, 1]

# For k=2, n=3
# Start at the first element.
# Look at that element and the following 2 and 
# put the smallest one in the current position.
# 

# off-by-one errors to look into: 
# - distance_from_current_position < max_distance
def quicker_sort(list_to_sort, max_distance):
    current_position = 0 # Increases to n
    while current_position < len(list_to_sort):
        smallest_element_position = current_position
        smallest_element_value = list_to_sort[current_position]
        
        distance_from_current_position = 0

        while distance_from_current_position <= max_distance:
            current_lookahead_position = current_position + distance_from_current_position
            if current_lookahead_position >= len(list_to_sort):
                break

            current_lookahead_value = list_to_sort[current_lookahead_position]

            if current_lookahead_value < smallest_element_value:
                smallest_element_position = current_lookahead_position
                smallest_element_value = current_lookahead_value

            distance_from_current_position += 1

        # Swap the values
        current_position_old_value = list_to_sort[current_position]
        list_to_sort[current_position] = smallest_element_value
        list_to_sort[smallest_element_position] = current_position_old_value

        current_position += 1

    return list_to_sort

#print(quicker_sort([4, 1, 3, 2], 3))
#print(quicker_sort([2, 1, 4, 3], 1))
#print(quicker_sort([2, 1], 1))
print(quicker_sort([1], 0))