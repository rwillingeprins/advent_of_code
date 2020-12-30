class Tile:
    def __init__(self, tile_id, pixels):
        self.id = tile_id
        self.pixels = pixels
        self.is_flipped = False

    def __str__(self):
        string = f'Tile {self.id}:\n'
        string += '\n'.join(''.join(row) for row in self.pixels)
        return string

    @property
    def right_border(self):
        return tuple(row[-1] for row in self.pixels)

    @property
    def bottom_border(self):
        return self.pixels[-1]

    @property
    def left_border(self):
        return tuple(row[0] for row in self.pixels)

    @property
    def top_border(self):
        return self.pixels[0]

    @property
    def borders(self):
        return [self.right_border, self.bottom_border, self.left_border, self.top_border]

    def transpose(self):
        self.pixels = tuple(row for row in zip(*self.pixels))

    def flip(self):
        self.pixels = self.pixels[::-1]

    def reorient(self):
        self.transpose() if self.is_flipped else self.flip()
        self.is_flipped = not self.is_flipped


with open('input/day20.txt') as file:
    tile_strings = file.read().split('\n\n')
tile_per_id = {}
tile_set_per_border = {}
for tile_string in tile_strings:
    title, *pixel_lines = tile_string.splitlines()
    tile_id = int(title.replace('Tile ', '').replace(':', ''))
    pixels = tuple(tuple(line) for line in pixel_lines)
    tile = Tile(tile_id, pixels)
    tile_per_id[tile_id] = tile
    for border in tile.borders:
        tile_set_per_border.setdefault(border, set())
        tile_set_per_border[border].add(tile)
        flipped_border = border[::-1]
        tile_set_per_border.setdefault(flipped_border, set())
        tile_set_per_border[flipped_border].add(tile)
images_tiles = []
for tile_id, tile in tile_per_id.items():
    unique_borders = []
    for border in tile.borders:
        if tile_set_per_border[border] == {tile}:
            unique_borders.append(border)
    if len(unique_borders) == 2:
        unique_border_set = set(unique_borders + [border[::-1] for border in unique_borders])
        while tile.left_border not in unique_border_set or tile.top_border not in unique_border_set:
            tile.reorient()
        images_tiles.append([tile])
        break
while True:
    tile = images_tiles[-1][-1]
    neighbor_tile_set = tile_set_per_border[tile.right_border] - {tile}
    if neighbor_tile_set:
        next_tile, = neighbor_tile_set
        while tile.right_border != next_tile.left_border:
            next_tile.reorient()
        images_tiles[-1].append(next_tile)
    else:
        tile = images_tiles[-1][0]
        neighbor_tile_set = tile_set_per_border[tile.bottom_border] - {tile}
        if neighbor_tile_set:
            next_tile, = neighbor_tile_set
            while tile.bottom_border != next_tile.top_border:
                next_tile.reorient()
            images_tiles.append([next_tile])
        else:
            break


def day20a():
    return images_tiles[0][0].id * images_tiles[0][-1].id * images_tiles[-1][0].id * images_tiles[-1][-1].id


def day20b():
    image_pixels = []
    for horizontal_tiles in images_tiles:
        for base_row_index in range(1, len(horizontal_tiles[0].pixels) - 1):
            pixel_row = []
            for tile in horizontal_tiles:
                pixel_row.extend(tile.pixels[base_row_index][1:-1])
            image_pixels.append(pixel_row)
    image = Tile(None, image_pixels)
    sea_monster = (
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    )
    sea_monster_relative_coordinates = []
    for base_row_index, sea_monster_string in enumerate(sea_monster):
        for base_col_index, pixel in enumerate(sea_monster_string):
            if pixel == '#':
                sea_monster_relative_coordinates.append((base_row_index, base_col_index))
    sea_monster_coordinate_set = set()
    while len(sea_monster_coordinate_set) == 0:
        image.reorient()
        for base_row_index in range(len(image.pixels) - len(sea_monster)):
            for base_col_index in range(len(image.pixels[0]) - len(sea_monster[0])):
                sea_monster_coordinates = [
                    (base_row_index + relative_row_index, base_col_index + relative_col_index)
                    for relative_row_index, relative_col_index in sea_monster_relative_coordinates
                ]
                if all(image.pixels[row_index][col_index] == '#' for row_index, col_index in sea_monster_coordinates):
                    sea_monster_coordinate_set.update(sea_monster_coordinates)
    water_roughness = 0
    for row_index, pixel_row in enumerate(image.pixels):
        for col_index, pixel in enumerate(pixel_row):
            if pixel == '#' and (row_index, col_index) not in sea_monster_coordinate_set:
                water_roughness += 1
    return water_roughness


print(day20a())
print(day20b())
