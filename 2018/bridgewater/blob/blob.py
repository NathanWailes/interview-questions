

def find_the_edges_by_searching_for_each_edge_at_a_time(list_of_lists_of_bools):
    """ This version does the very-straightforward approach of first looking for the top edge, then the bottom edge,
    then the left edge, and then the right edge. It doesn't have any logic to avoid reading the same cell multiple
    times.

    :param list_of_lists_of_bools:
    :return:
    """
    input_side_length = len(list_of_lists_of_bools)

    cell_reads = 0
    top = 9
    left = 9
    bottom = 0
    right = 0

    # Find the top edge.
    for row_index, row in enumerate(list_of_lists_of_bools):
        found_a_blob_section = False

        for column_index, cell_has_a_blob_section in enumerate(row):
            cell_reads += 1
            if cell_has_a_blob_section:
                found_a_blob_section = True
                top = row_index
                break

        if found_a_blob_section:
            break

    # Find the bottom edge.
    for row_index, row in reverse_enumerate(list_of_lists_of_bools):
        found_a_blob_section = False

        for column_index, cell_has_a_blob_section in enumerate(row):
            cell_reads += 1
            if cell_has_a_blob_section:
                found_a_blob_section = True
                bottom = row_index
                break

        if found_a_blob_section:
            break

    # Find the left edge.
    for column_index in range(input_side_length):  # Assumes the area to be searched is square-shaped.
        found_a_blob_section = False
        for row_index in range(input_side_length):
            cell_has_a_blob_section = list_of_lists_of_bools[row_index][column_index]
            cell_reads += 1

            if cell_has_a_blob_section:
                found_a_blob_section = True
                left = column_index
                break

        if found_a_blob_section:
            break

    # Find the right edge.
    for column_index in range(input_side_length - 1, 0, -1):  # Assumes the area to be searched is square-shaped.
        found_a_blob_section = False
        for row_index in range(input_side_length):
            cell_has_a_blob_section = list_of_lists_of_bools[row_index][column_index]
            cell_reads += 1

            if cell_has_a_blob_section:
                found_a_blob_section = True
                right = column_index
                break

        if found_a_blob_section:
            break

    return cell_reads, top, left, bottom, right


def reverse_enumerate(obj, start=0):
    for index in range(len(obj)-start-1, -1, -1):
        yield index, obj[index]


def find_the_edges_by_searching_for_every_edge_simultaneously(list_of_lists_of_bools):
    """ This code is a little shorter but I think it's much harder to understand. I would stick with the other version.

    All it does is combine the four double-nested loops in the first version; there are four iterators that start in the
    four corners, and then move clockwise. The original idea was to 1) have the four iterators not read the cells read
    by the other iterators, and 2) continue to have the iterators stop reading cells once they found the edge for their
    side (as happens in the first version, above). But then I realized that a working approach could not afford to
    combine those two constraints, so now it's just a harder-to-read version of the initial solution I came up with.

    :param list_of_lists_of_bools:
    :return:
    """
    input_side_length = len(list_of_lists_of_bools)
    max_index = input_side_length - 1

    cell_reads = 0

    edge_index_for = {
        'top': 9,
        'bottom': 0,
        'left': 9,
        'right': 0,
    }

    found_the_edge_for = {
        'top': False,
        'bottom': False,
        'left': False,
        'right': False,
     }

    all_sides_found = found_the_edge_for['top'] and found_the_edge_for['bottom'] and found_the_edge_for['left'] and \
                      found_the_edge_for['right']

    slow_incrementer = 0  # This increments the row for the top/bottom edges and the column for the left/right edges

    while slow_incrementer <= max_index and not all_sides_found:
        fast_incrementer = 0  # This increments the column for the top/bottom edges and the row for the left/right edges

        while fast_incrementer <= max_index and not all_sides_found:

            for side in ['top', 'left', 'right', 'bottom']:
                if not found_the_edge_for[side]:
                    row_index = get_row_index(side, slow_incrementer, fast_incrementer, max_index)
                    column_index = get_column_index(side, slow_incrementer, fast_incrementer, max_index)

                    cell_has_a_blob_section = list_of_lists_of_bools[row_index][column_index]
                    cell_reads += 1

                    if cell_has_a_blob_section:
                        found_the_edge_for[side] = True
                        if side in ['top', 'bottom']:
                            edge_index_for[side] = row_index
                        else:
                            edge_index_for[side] = column_index

            fast_incrementer += 1

            all_sides_found = found_the_edge_for['top'] and found_the_edge_for['bottom'] and found_the_edge_for['left'] and found_the_edge_for['right']

        slow_incrementer += 1

    return cell_reads, edge_index_for


def get_row_index(side, slow_incrementer, fast_incrementer, max_index):
    row_index_for = {
        'top': slow_incrementer,
        'bottom': max_index - slow_incrementer,
        'left': max_index - fast_incrementer,
        'right': fast_incrementer,
    }
    return row_index_for[side]


def get_column_index(side, slow_incrementer, fast_incrementer, max_index):
    column_index_for = {
        'top': fast_incrementer,
        'bottom': max_index - fast_incrementer,
        'left': slow_incrementer,
        'right': max_index - slow_incrementer,
    }
    return column_index_for[side]


if __name__ == "__main__":
    input_as_a_string = """ 0000000000
                            0011100000
                            0011111000
                            0010001000
                            0011111000
                            0000101000
                            0000101000
                            0000111000
                            0000000000
                            0000000000"""

    input_as_a_string = input_as_a_string.replace(" ", "")
    input_as_a_list_of_strings = input_as_a_string.split("\n")

    input_as_a_list_of_lists_of_bools = []
    for current_line_as_a_string in input_as_a_list_of_strings:
        list_of_bools = []

        for character in current_line_as_a_string:
            list_of_bools.append(bool(int(character)))

        input_as_a_list_of_lists_of_bools.append(list_of_bools)

    print(find_the_edges_by_searching_for_each_edge_at_a_time(input_as_a_list_of_lists_of_bools))
    print(find_the_edges_by_searching_for_every_edge_simultaneously(input_as_a_list_of_lists_of_bools))
