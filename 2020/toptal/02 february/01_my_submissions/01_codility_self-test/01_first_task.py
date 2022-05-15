"""
There are two possible configurations in which a family of four can be in a row.
In the first configuration, a single family of four is in the center group.  This is
ideal if one of the two side groups has a reservation in one of the two seats closest
to the aisle.
In the second configuration, two families of four are in a single row.  This configuration
is ideal if neither side group of seats has a reservation in the two seats closest to the
aisle.
"""


def solution(N, S):
    reserved_seats_by_row = get_reservations_as_a_list_of_lists(N, S)
    number_of_four_person_families_that_can_be_seated_together = 0
    for current_row_reserved_seats in reserved_seats_by_row:
        if we_can_place_two_families_in_the_row(current_row_reserved_seats):
            number_of_four_person_families_that_can_be_seated_together += 2
        elif we_can_place_a_family_in_the_middle(current_row_reserved_seats):
            number_of_four_person_families_that_can_be_seated_together += 1
        elif we_can_place_a_family_on_the_left(current_row_reserved_seats):
            number_of_four_person_families_that_can_be_seated_together += 1
        elif we_can_place_a_family_on_the_right(current_row_reserved_seats):
            number_of_four_person_families_that_can_be_seated_together += 1
    return number_of_four_person_families_that_can_be_seated_together


def get_reservations_as_a_list_of_lists(N, S):
    reservations = S.split()  # ['1A', '2F', '1C']
    rows_to_list_of_reserved_seats = [set() for row_index in range(N)]  # We want: [[0, 2], [5]]
    for reservation in reservations:
        row_index = int(reservation[:-1]) - 1  # '412F' --> 411
        seat_letter = reservation[-1:]  # '412F' --> 'F'
        seat_index = get_seat_index_from_seat_letter(seat_letter)
        rows_to_list_of_reserved_seats[row_index].add(seat_index)
    return rows_to_list_of_reserved_seats


def get_seat_index_from_seat_letter(seat_letter):
    if seat_letter == 'A':
        return 0
    elif seat_letter == 'B':
        return 1
    elif seat_letter == 'C':
        return 2
    elif seat_letter == 'D':
        return 3
    elif seat_letter == 'E':
        return 4
    elif seat_letter == 'F':
        return 5
    elif seat_letter == 'G':
        return 6
    elif seat_letter == 'H':
        return 7
    elif seat_letter == 'J':
        return 8
    elif seat_letter == 'K':
        return 9


def we_can_place_two_families_in_the_row(current_row_reserved_seats):
    if not current_row_reserved_seats:
        return True
    for seat_index in range(1, 9):
        if seat_index in current_row_reserved_seats:
            return False
    return True


def we_can_place_a_family_in_the_middle(current_row_reserved_seats):
    for seat_index in range(3, 7):
        if seat_index in current_row_reserved_seats:
            return False
    return True


def we_can_place_a_family_on_the_left(current_row_reserved_seats):
    for seat_index in range(1, 5):
        if seat_index in current_row_reserved_seats:
            return False
    return True


def we_can_place_a_family_on_the_right(current_row_reserved_seats):
    for seat_index in range(5, 9):
        if seat_index in current_row_reserved_seats:
            return False
    return True


if __name__ == '__main__':
    assert(solution(2, "1A 2F 1C") == 2)
    assert(solution(1, "") == 2)
    assert(solution(50, "49A 50F 49A") == 2)
