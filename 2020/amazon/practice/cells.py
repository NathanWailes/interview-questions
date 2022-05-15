ACTIVE = 1
INACTIVE = 0


def cellCompete(current_states, days):
    new_states = [value for value in current_states]
    LAST_INDEX = len(current_states) - 1
    for day in range(days):
        current_states = [value for value in new_states]
        for index in range(len(current_states)):
            # Handle the edge-case of the first cell
            if index == 0:
                if len(current_states) > 1:
                    if current_states[1] == INACTIVE:
                        new_states[0] = INACTIVE
                    else:
                        new_states[0] = ACTIVE
                else:
                    # If there's only one cell, then both sides
                    # of it should be treated as inactive, which means
                    # the cell should be made inactive.
                    new_states[0] = INACTIVE
            # Edge-case: last cell
            elif index == LAST_INDEX:
                if len(current_states) > 1:
                    if current_states[LAST_INDEX - 1] == INACTIVE:
                        new_states[index] = INACTIVE
                    else:
                        new_states[index] = ACTIVE
                else:
                    pass  # It's been handled already as the first cell
            else:
                if current_states[index - 1] == current_states[index + 1]:
                    new_states[index] = INACTIVE
                else:
                    new_states[index] = ACTIVE

    return new_states


if __name__ == '__main__':
    print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))
    assert(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1) == [0, 1, 0, 0, 1, 0, 1, 0])

    print(cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2))
    assert(cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2) == [0, 0, 0, 0, 0, 1, 1, 0])
