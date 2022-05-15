def solution(A):
    modified_tree_heights = list.copy(A)
    minimum_height = min(A)
    shortest_tree_index = A.index(minimum_height)
    we_should_be_on_a_peak = True
    number_of_cuts = 0
    for tree_index in range(shortest_tree_index - 1, 0, -1):
        current_tree_height = A[tree_index]
        if we_should_be_on_a_peak:
            we_should_be_on_a_peak = False
            continue
        else:  # we should be in a valley
            if tree_index > 0:
                previous_tree_height = modified_tree_heights[tree_index + 1]
                if current_tree_height > previous_tree_height:
                    modified_tree_heights[tree_index] = previous_tree_height - 1
                    number_of_cuts += 1
    we_should_be_on_a_peak = True
    for tree_index in range(shortest_tree_index + 1, len(A)):
        current_tree_height = A[tree_index]
        if we_should_be_on_a_peak:
            we_should_be_on_a_peak = False
            continue
        else:  # we should be in a valley
            if tree_index < len(modified_tree_heights) - 1:
                previous_tree_height = modified_tree_heights[tree_index - 1]
                if current_tree_height > previous_tree_height:
                    modified_tree_heights[tree_index] = previous_tree_height - 1
                    number_of_cuts += 1
    return number_of_cuts


if __name__ == '__main__':
    # print(solution([5, 4, 3, 2, 6]))
    # print(solution([3, 7, 4, 5]))
    assert(solution([5, 4, 3, 2, 6]) == 1)
    assert(solution([3, 7, 4, 5]) == 0)
