import random
from collections import namedtuple


Cell = namedtuple('Cell', ['x', 'y'])


def generate_an_area_where_each_cell_has_a_fifty_percent_chance_of_being_occupied():
    output = []

    for i in range(10):
        new_line_of_output = []
        for j in range(10):
            new_line_of_output.append(str(random.choice([0, 1])))
        output.append(new_line_of_output)

    return output


def get_empty_square_2D_array_of_size_n(side_length=10):
    grid = []
    for i in range(side_length):
        new_line_of_output = []
        for j in range(side_length):
            new_line_of_output.append(0)
        grid.append(new_line_of_output)
    return grid


def generate_an_area_where_each_cell_adjacent_to_a_blob_has_a_fifty_percent_chance_of_becoming_occupied():
    ten_by_ten_array = get_empty_square_2D_array_of_size_n(10)

    # Place the initial cell
    initial_cell_row = random.randint(0, 9)
    initial_cell_column = random.randint(0, 9)
    ten_by_ten_array[initial_cell_row][initial_cell_column] = 1

    cells_to_check_neighbors_for = [
        [initial_cell_row, initial_cell_column]
    ]

    second_cell_options = []
    for row_offset in [1, 0, -1]:
        for column_offset in [1, 0, -1]:
            # Neighbor cells are those to the top, left, bottom, or right of the current cell to check neighbors for
            if not abs(row_offset) + abs(column_offset) == 1:
                continue

            cell_row = initial_cell_row + row_offset
            cell_column = initial_cell_column + column_offset

            if cell_row in range(10) and cell_column in range(10):
                second_cell_options.append([cell_row, cell_column])

    second_cell_coordinates = random.choice(second_cell_options)
    ten_by_ten_array[second_cell_coordinates[0]][second_cell_coordinates[1]] = 1  # Place the second cell

    cells_considered = ten_by_ten_array[:]

    # Place the third, fourth, fifth, etc. cell
    i = 0
    while i < len(cells_to_check_neighbors_for):
        current_cell = cells_to_check_neighbors_for[i]

        for row_offset in [1, 0, -1]:
            for column_offset in [1, 0, -1]:
                # Neighbor cells are those to the top, left, bottom, or right of the current cell to check neighbors for
                if not abs(row_offset) + abs(column_offset) == 1:
                    continue

                potential_neighbor_cell_row = current_cell[0] + row_offset
                potential_neighbor_cell_column = current_cell[1] + column_offset

                # If the coordinates are off the 10x10 grid, it's not a valid neighbor.
                if potential_neighbor_cell_row not in range(10) or potential_neighbor_cell_column not in range(10):
                    continue

                # We only want to consider any particular cell once.
                if cells_considered[potential_neighbor_cell_row][potential_neighbor_cell_column] == 1:
                    continue

                cells_considered[potential_neighbor_cell_row][potential_neighbor_cell_column] = 1

                if random.random() < 0.6:
                    cells_to_check_neighbors_for.append([potential_neighbor_cell_row, potential_neighbor_cell_column])

                    ten_by_ten_array[potential_neighbor_cell_row][potential_neighbor_cell_column] = 1
        i += 1

    ten_by_ten_array = [[str(cell) for cell in line] for line in ten_by_ten_array]  # Convert cells to strings.

    return ten_by_ten_array


def get_blob_size():
    blob_size = 0
    for i in range(100):
        if random.random() < .5:
            blob_size += 1

    return blob_size


def generate_blob_of_size_n(desired_blob_size):
    """
    A potential problem with this approach is that the blobs frequently stretch out across the wall.
    :param desired_blob_size:
    :return:
    """
    ten_by_ten_array = get_empty_square_2D_array_of_size_n(10)

    # Place the initial cell
    last_added_cell_row = random.randint(0, 9)
    last_added_cell_column = random.randint(0, 9)
    ten_by_ten_array[last_added_cell_row][last_added_cell_column] = 1

    neighboring_cells = set()

    # We're going to pop this new entry out immediately, this line is just to get the 'while' loop working properly.
    neighboring_cells.add((last_added_cell_row, last_added_cell_column))

    current_blob_size = 1
    while current_blob_size < desired_blob_size:
        new_cell_coordinates = []

        # Once we add a cell to the blob, it's no longer a 'neighboring' cell.
        neighboring_cells.remove((last_added_cell_row, last_added_cell_column))

        # Add the cells neighboring the last-added cell to the set of neighbors
        for row_offset in [1, 0, -1]:
            for column_offset in [1, 0, -1]:
                # Neighbor cells are those to the top, left, bottom, or right of the current cell to check neighbors for
                if not abs(row_offset) + abs(column_offset) == 1:
                    continue

                cell_row = last_added_cell_row + row_offset
                cell_column = last_added_cell_column + column_offset

                if cell_row in range(10) and cell_column in range(10):
                    neighboring_cells.add((cell_row, cell_column))

        # Pick one of the neighboring cells to be the added to the blob.
        new_cell = random.sample(neighboring_cells, 1)[0]

        # Add it to the blob
        ten_by_ten_array[new_cell[0]][new_cell[1]] = 1

        # Track the new cell's coordinates so we can remove it from the set of neighboring cells.
        last_added_cell_row = new_cell[0]
        last_added_cell_column = new_cell[1]

        current_blob_size += 1

    ten_by_ten_array = [[str(cell) for cell in line] for line in ten_by_ten_array]  # Convert cells to strings.

    return ten_by_ten_array


def pick_a_blob_uniformly():
    """
    Implements the method suggested here: https://math.stackexchange.com/a/2550968/510058
    :return:
    """
    while True:
        # Randomly choose which 100 cells are occupied
        randomly_filled_in_grid = generate_an_area_where_each_cell_has_a_fifty_percent_chance_of_being_occupied()

        # Choose a cell uniformly at random
        selected_cell = Cell(x=random.randint(0, 9), y=random.randint(0, 9))

        # If it's not occupied, start over.
        if not randomly_filled_in_grid[selected_cell.y][selected_cell.x]:
            continue

        # If it's not part of a blob, start over.
        set_of_connected_points, neighboring_cells = get_blob_and_neighbors(selected_cell, randomly_filled_in_grid)
        size_of_the_blob = len(set_of_connected_points)
        if size_of_the_blob < 2:
            continue

        probability_of_this_blob = (size_of_the_blob / 100) * pow((1/2), size_of_the_blob + len(neighboring_cells))

        probability_of_the_rarest_blobs = (33 / 100) * pow(1 / 2, 100)
        acceptance_probability = probability_of_the_rarest_blobs / probability_of_this_blob

        if random.random() <= acceptance_probability:
            # Use this one
            grid_with_blob_in_it = get_empty_square_2D_array_of_size_n(10)
            for cell in set_of_connected_points:
                grid_with_blob_in_it[cell.y][cell.x] = 1
            break

    return grid_with_blob_in_it


def get_blob_and_neighbors(starting_point, grid):
    blob = {starting_point}
    list_of_blob_cells_we_still_need_to_check_neighbors_for = [starting_point]

    set_of_neighboring_cells = set()

    # Get the first point.
    # Add its neighbors to a list of neighbors to look into
    # For each entry in the list of neighbors
    #  If it's occupied, add it to the set of occupied spaces and add its neighbors to the list if they're not part of
    #  the blob

    while list_of_blob_cells_we_still_need_to_check_neighbors_for:
        blob_cell_to_check_neighbors_for = list_of_blob_cells_we_still_need_to_check_neighbors_for.pop()

        for (row_offset, column_offset) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                cell_row = blob_cell_to_check_neighbors_for.y + row_offset
                cell_column = blob_cell_to_check_neighbors_for.x + column_offset

                current_cell = Cell(cell_column, cell_row)

                # If it's off-the-grid, skip it.
                if cell_row not in range(10) or cell_column not in range(10):
                    continue

                # If we've already seen this one, skip it.
                if current_cell in blob or current_cell in set_of_neighboring_cells:
                    continue

                is_occupied = bool(int((grid[current_cell.y][current_cell.x])))

                # If it's not occupied, add it to the set of neighbors
                if not is_occupied:
                    set_of_neighboring_cells.add(current_cell)
                else:
                    # If it is occupied, add it to the blob and add it to the list of cells to check neighbors for
                    blob.add(current_cell)
                    list_of_blob_cells_we_still_need_to_check_neighbors_for.append(current_cell)

    return blob, set_of_neighboring_cells


if __name__ == '__main__':
    # output = generate_an_area_where_each_cell_has_a_fifty_percent_chance_of_being_occupied()

    output = pick_a_blob_uniformly()

    for line in output:
        print("  ".join([str(cell) for cell in line]))
