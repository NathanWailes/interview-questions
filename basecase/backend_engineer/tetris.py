import random
from collections import namedtuple


MOVE_LEFT = "a"
MOVE_RIGHT = "d"
MOVE_CLOCKWISE = "s"
MOVE_COUNTERCLOCKWISE = "w"


class GameOverException(Exception):
    def __init__(self, message="", errors=[]):
        super().__init__(message)
        self.errors = errors


Point = namedtuple("Point", ["x", "y"])


class Tetris:
    def __init__(self):
        self.board = Board()
        self.current_piece = None

    def play_game(self):
        while True:
            try:
                self._step()
            except GameOverException:
                # We need to draw the board one last time or the last move won't be displayed, because the board is
                # normally drawn right before asking for user input, *after* having placed any new piece, but the
                # GameOverException will get raised when trying to place the new piece.
                self._draw_board()

                print("\nGame over.")
                break

    def _step(self):
        if not self.current_piece or not self.current_piece.get_valid_moves():
            try:
                self.current_piece = self.board.place_new_piece()
            except GameOverException:
                raise

        selected_move = self._get_user_input()

        self._update_board(selected_move)

    def _get_user_input(self):
        selection_was_invalid = False
        while True:
            self._draw_board()
            valid_moves = self.current_piece.get_valid_moves()

            presented_options = ""
            if MOVE_LEFT in valid_moves:
                presented_options += "a - move piece left\n"
            if MOVE_RIGHT in valid_moves:
                presented_options += "d - move piece right\n"
            if MOVE_CLOCKWISE in valid_moves:
                presented_options += "s - rotate piece clockwise\n"
            if MOVE_COUNTERCLOCKWISE in valid_moves:
                presented_options += "w - rotate piece counter clockwise\n"
            print("Select your next move:\n"
                  "\n" +
                  presented_options)

            if selection_was_invalid:
                print("Your last selection was invalid.\n")

            print("Choice: ", end="")

            user_input = input()
            if user_input not in valid_moves:
                selection_was_invalid = True
            else:
                break
        return user_input

    def _draw_board(self):
        print(self.board.get_displayed_board())

    def _update_board(self, selected_move):
        for x, y in self.current_piece.occupied_coordinates:
            self.board.clear_position(x, y)

        current_x_position = self.current_piece.current_position.x

        if selected_move == MOVE_RIGHT:
            new_occupied_coordinates = self.current_piece.get_moved_right_position()
            current_x_position += 1
        elif selected_move == MOVE_LEFT:
            new_occupied_coordinates = self.current_piece.get_moved_left_position()
            current_x_position -= 1
        elif selected_move == MOVE_CLOCKWISE:
            new_occupied_coordinates = self.current_piece.get_rotated_clockwise_position()
            self.current_piece.orientation = self.current_piece.get_rotated_cw_orientation()
        elif selected_move == MOVE_COUNTERCLOCKWISE:
            new_occupied_coordinates = self.current_piece.get_rotated_ccw_position()
            self.current_piece.orientation = self.current_piece.get_rotated_ccw_orientation()
        else:
            raise ValueError

        # The current_position is used to make calculating rotations easier.
        self.current_piece.current_position = Point(current_x_position, self.current_piece.current_position.y + 1)

        for x, y in new_occupied_coordinates:
            self.board.set_position_to_occupied(x, y)

        self.current_piece.occupied_coordinates = new_occupied_coordinates


class Board:
    playable_area_width = 20
    playable_area_height = 20

    def __init__(self):
        self.playable_area = [[" " for i in range(Board.playable_area_width)] for j in range(Board.playable_area_height)]

    def get_displayed_board(self):
        displayed_board = "\n".join(["*" + "".join(line) + "*" for line in self.playable_area])

        # Add the bottom row of asterisks
        displayed_board += "\n" + "".join(["*" for j in range(Board.playable_area_width + 2)])  # Add 2 for the walls
        return displayed_board

    def place_new_piece(self):
        """ a new piece appears along the top of the board, randomly positioned along the x-axis.

        :param piece:
        :return:
        """
        piece = Piece.get_random_unplaced_piece(self)
        x_offset = self._get_random_x_offset_for_new_piece(piece)
        piece.current_position = Point(x_offset, 0)

        for y_index, line in enumerate(piece.piece_type.default_appearance):
            for x_index, character in enumerate(line):
                if character == "*" and self.playable_area[y_index][x_offset + x_index] != " ":
                    raise GameOverException
                self.playable_area[y_index][x_offset + x_index] = character

                if character == "*":
                    piece.occupied_coordinates.append((x_offset + x_index, y_index))

        return piece

    def _get_random_x_offset_for_new_piece(self, piece):
        width_of_the_piece = len(piece.piece_type.default_appearance[0])  # This grabs the first row of the 2D array
        max_possible_x_offset = Board.playable_area_width - width_of_the_piece
        x_offset = random.randint(0, max_possible_x_offset)
        return x_offset

    def position_is_available(self, list_of_coordinates, piece):
        if not list_of_coordinates:
            return False

        for x, y in list_of_coordinates:
            if x < 0 or x > 19 or y < 0 or y > 19 or (self.playable_area[y][x] != " "
                                                      and (x, y) not in piece.occupied_coordinates):
                return False
        return True

    def clear_position(self, x, y):
        self.playable_area[y][x] = " "

    def set_position_to_occupied(self, x, y):
        self.playable_area[y][x] = "*"


class Piece:
    PieceType = namedtuple("PieceType", ['name', 'default_appearance'])
    I = PieceType(name="I", default_appearance=[["*", "*", "*", "*"]])
    L = PieceType(name="L", default_appearance=[["*", " "],
                                                ["*", " "],
                                                ["*", "*"]])
    J = PieceType(name="J", default_appearance=[[" ", "*"],
                                                [" ", "*"],
                                                ["*", "*"]])
    Z = PieceType(name="Z", default_appearance=[[" ", "*"],
                                                ["*", "*"],
                                                ["*", " "]])
    O = PieceType(name="square", default_appearance=[["*", "*"],
                                                     ["*", "*"]])
    piece_types = [I, L, J, Z, O]

    DEFAULT_ORIENTATION = 0
    NINETY_DEGREES_CLOCKWISE = 1
    ONE_HUNDRED_EIGHTY_DEGREES_CLOCKWISE = 2
    TWO_HUNDRED_SEVENTY_DEGREES_CLOCKWISE = 3

    def __init__(self, piece_type, board):
        self.piece_type = piece_type
        self.board = board
        self.orientation = Piece.DEFAULT_ORIENTATION
        self.occupied_coordinates = []  # This is set in Board.place_new_piece()
        self.current_position = None  # This is set in Board.place_new_piece()

    @staticmethod
    def get_random_unplaced_piece(board):
        new_piece = Piece(random.choice(Piece.piece_types), board)
        return new_piece

    def get_moved_left_position(self):
        """ This function returns the list of coordinates that will be occupied by this piece if the user chooses the
        specified action.  It *will* return invalid positions.

        :return:
        """
        return [(x - 1, y + 1) for x, y in self.occupied_coordinates]

    def get_moved_right_position(self):
        """ This function returns the list of coordinates that will be occupied by this piece if the user chooses the
        specified action.  It *will* return invalid positions.

        :return:
        """
        return [(x + 1, y + 1) for x, y in self.occupied_coordinates]

    def get_rotated_clockwise_position(self):
        """ This function returns the list of coordinates that will be occupied by this piece if the user chooses the
        specified action.  It *will* return invalid positions.

        :return:
        """
        new_orientation = self.get_rotated_cw_orientation()
        return self.get_position_after_move_given_new_orientation(new_orientation)

    def get_rotated_ccw_position(self):
        """ This function returns the list of coordinates that will be occupied by this piece if the user chooses the
        specified action.  It *will* return invalid positions.

        :return:
        """
        new_orientation = self.get_rotated_ccw_orientation()
        return self.get_position_after_move_given_new_orientation(new_orientation)

    def get_position_after_move_given_new_orientation(self, new_orientation):
        """ The canonical x and y position of a piece are defined by the top-left corner of the "default_appearance"
        in the namedtuple for each piece type.

        Also, y increases as you go further down the board. So the top of the board is y=0, the bottom is y=19.

        This code is not beautiful, but it works.

        :param new_orientation:
        :return:
        """
        xpos = self.current_position.x
        ypos = self.current_position.y

        if self.piece_type.name == "I":
            if new_orientation in [Piece.DEFAULT_ORIENTATION, Piece.ONE_HUNDRED_EIGHTY_DEGREES_CLOCKWISE]:
                return [(xpos, ypos + 1), (xpos + 1, ypos + 1), (xpos + 2, ypos + 1), (xpos + 3, ypos + 1)]
            else:
                return [(xpos + 2, ypos - 1), (xpos + 2, ypos), (xpos + 2, ypos + 1), (xpos + 2, ypos + 2)]

        if self.piece_type.name == "L":
            if new_orientation == Piece.DEFAULT_ORIENTATION:
                return [(xpos, ypos + 1), (xpos, ypos + 2), (xpos, ypos + 3), (xpos + 1, ypos + 3)]
            elif new_orientation == Piece.NINETY_DEGREES_CLOCKWISE:
                return [(xpos - 1, ypos + 2), (xpos - 1, ypos + 3), (xpos, ypos + 2), (xpos + 1, ypos + 2)]
            elif new_orientation == Piece.ONE_HUNDRED_EIGHTY_DEGREES_CLOCKWISE:
                return [(xpos, ypos + 1), (xpos, ypos + 2), (xpos, ypos + 3), (xpos - 1, ypos + 1)]
            elif new_orientation == Piece.TWO_HUNDRED_SEVENTY_DEGREES_CLOCKWISE:
                return [(xpos - 1, ypos + 3), (xpos, ypos + 3), (xpos + 1, ypos + 2), (xpos + 1, ypos + 3)]
            else:
                raise ValueError

        if self.piece_type.name == "J":
            if new_orientation == Piece.DEFAULT_ORIENTATION:
                return [(xpos + 1, ypos + 1), (xpos + 1, ypos + 2), (xpos + 1, ypos + 3), (xpos, ypos + 3)]
            elif new_orientation == Piece.NINETY_DEGREES_CLOCKWISE:
                return [(xpos, ypos + 2), (xpos, ypos + 3), (xpos + 1, ypos + 3), (xpos + 2, ypos + 3)]
            elif new_orientation == Piece.ONE_HUNDRED_EIGHTY_DEGREES_CLOCKWISE:
                return [(xpos + 1, ypos + 1), (xpos + 1, ypos + 2), (xpos + 1, ypos + 3), (xpos + 2, ypos + 1)]
            elif new_orientation == Piece.TWO_HUNDRED_SEVENTY_DEGREES_CLOCKWISE:
                return [(xpos, ypos + 2), (xpos + 1, ypos + 2), (xpos + 2, ypos + 2), (xpos + 2, ypos + 3)]
            else:
                raise ValueError

        if self.piece_type.name == "Z":
            if new_orientation in [Piece.DEFAULT_ORIENTATION, Piece.ONE_HUNDRED_EIGHTY_DEGREES_CLOCKWISE]:
                return [(xpos, ypos + 3), (xpos, ypos + 2), (xpos + 1, ypos + 2), (xpos + 1, ypos + 1)]
            else:
                return [(xpos - 1, ypos + 2), (xpos, ypos + 2), (xpos, ypos + 3), (xpos + 1, ypos + 3)]

        if self.piece_type.name == "O":
            return [(x, y + 1) for x, y in self.occupied_coordinates]
        return []

    def get_rotated_cw_orientation(self):
        rotated_orientation = self.orientation + 1
        if rotated_orientation > Piece.TWO_HUNDRED_SEVENTY_DEGREES_CLOCKWISE:
            rotated_orientation = Piece.DEFAULT_ORIENTATION
        return rotated_orientation

    def get_rotated_ccw_orientation(self):
        rotated_orientation = self.orientation - 1
        if rotated_orientation < Piece.DEFAULT_ORIENTATION:
            rotated_orientation = Piece.TWO_HUNDRED_SEVENTY_DEGREES_CLOCKWISE
        return rotated_orientation

    def get_valid_moves(self):
        """

        :param self:
        :return:
        """
        valid_moves =[]

        if self.board.position_is_available(self.get_moved_left_position(), self):
            valid_moves.append(MOVE_LEFT)

        if self.board.position_is_available(self.get_moved_right_position(), self):
            valid_moves.append(MOVE_RIGHT)

        if self.board.position_is_available(self.get_rotated_clockwise_position(), self):
            valid_moves.append(MOVE_CLOCKWISE)

        if self.board.position_is_available(self.get_rotated_ccw_position(), self):
            valid_moves.append(MOVE_COUNTERCLOCKWISE)

        return valid_moves


if __name__ == "__main__":
    new_game = Tetris()
    new_game.play_game()
