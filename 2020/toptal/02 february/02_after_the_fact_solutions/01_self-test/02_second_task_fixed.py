def solution(A):
    modified_tree_heights = list.copy(A)
    minimum_height = min(A)
    shortest_tree_index = A.index(minimum_height)
    we_should_be_on_a_peak = True
    trees_to_cut = set()
    for tree_index in range(shortest_tree_index - 1, 0, -1):
        current_tree_height = A[tree_index]
        if we_should_be_on_a_peak:
            if tree_index < len(modified_tree_heights) - 1:
                previous_tree_height = modified_tree_heights[tree_index - 1]
                if current_tree_height <= previous_tree_height:
                    modified_tree_heights[tree_index - 1] = current_tree_height - 1
                    trees_to_cut.add(tree_index - 1)
            we_should_be_on_a_peak = False
        else:  # we should be in a valley
            if tree_index > 0:
                previous_tree_height = modified_tree_heights[tree_index + 1]
                if current_tree_height >= previous_tree_height:
                    modified_tree_heights[tree_index] = previous_tree_height - 1
                    trees_to_cut.add(tree_index)
            we_should_be_on_a_peak = True
    we_should_be_on_a_peak = True
    for tree_index in range(shortest_tree_index + 1, len(A)):
        current_tree_height = A[tree_index]
        if we_should_be_on_a_peak:
            if tree_index < len(modified_tree_heights) - 1:
                previous_tree_height = modified_tree_heights[tree_index - 1]
                if current_tree_height <= previous_tree_height:
                    modified_tree_heights[tree_index - 1] = current_tree_height - 1
                    trees_to_cut.add(tree_index - 1)
            we_should_be_on_a_peak = False
        else:  # we should be in a valley
            if tree_index < len(modified_tree_heights) - 1:
                previous_tree_height = modified_tree_heights[tree_index - 1]
                if current_tree_height >= previous_tree_height:
                    modified_tree_heights[tree_index] = previous_tree_height - 1
                    trees_to_cut.add(tree_index)
            we_should_be_on_a_peak = True
    return len(trees_to_cut)


if __name__ == '__main__':
    # print(solution([5, 4, 3, 2, 6]))
    # print(solution([3, 7, 4, 5]))
    assert(solution([5, 4, 3, 2, 6]) == 1)
    assert(solution([3, 7, 4, 5]) == 0)
    assert(solution([4, 4, 4, 4]) == 2)
