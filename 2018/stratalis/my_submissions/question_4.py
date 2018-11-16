class Tile:
    previous_tile = None
    next_tile = None

    def __init__(self, value):
        self.value = value

    def set_previous_tile(self, previous_tile):
        self.previous_tile = previous_tile

    def set_next_tile(self, next_tile):
        self.next_tile = next_tile


class Platformer:

    tiles = []

    def __init__(self, initial_number_of_tiles, initial_index_of_the_character):
        """
        :param initial_number_of_tiles: (int) The initial number of tiles.
        :param initial_index_of_the_character: (int) The initial position of the character.
        """

        for tile_value in list(range(initial_number_of_tiles)):
            new_tile = Tile(tile_value)
            self.tiles.append(new_tile)

            if tile_value > 0:
                previous_tile = self.tiles[tile_value - 1]
                previous_tile.set_next_tile(new_tile)
                new_tile.set_previous_tile(previous_tile)

            if tile_value == initial_index_of_the_character:
                self.current_tile = new_tile
        self.tiles_are_unmodified = True

    def jump_left(self):
        tile_to_remove = self.current_tile
        self.current_tile = self.current_tile.next_tile.next_tile

        if tile_to_remove.previous_tile:
            tile_to_remove.previous_tile.next_tile = tile_to_remove.next_tile

        if tile_to_remove.next_tile:
            tile_to_remove.next_tile.previous_tile = tile_to_remove.previous_tile

    def jump_right(self):
        tile_to_remove = self.current_tile
        self.current_tile = self.current_tile.previous_tile.previous_tile

        if tile_to_remove.previous_tile:
            tile_to_remove.previous_tile.next_tile = tile_to_remove.next_tile

        if tile_to_remove.next_tile:
            tile_to_remove.next_tile.previous_tile = tile_to_remove.previous_tile

    def position(self):
        """
        :returns: (int) The position of the character.
        """
        return self.current_tile.value


platformer = Platformer(6, 3)
print(platformer.position())
platformer.jump_left()
print(platformer.position())
platformer.jump_right()
print(platformer.position())