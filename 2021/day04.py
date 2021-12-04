def get_draw_numbers_and_boards():
    with open('input/day04.txt') as file:
        draws_string, *board_strings = file.read().split('\n\n')
    draw_numbers = [int(draw_string) for draw_string in draws_string.split(',')]
    boards = [
        [
            [
                {'number': int(number_string), 'is_marked': False}
                for number_string in row_string.lstrip().split()
            ]
            for row_string in board_string.splitlines()
        ]
        for board_string in board_strings
    ]
    return draw_numbers, boards


def bingo(board, draw_number):
    for row_index, current_row in enumerate(board):
        for col_index, current_tile in enumerate(current_row):
            if current_tile['number'] == draw_number:
                current_tile['is_marked'] = True
                row_is_complete = all(tile['is_marked'] for tile in current_row)
                column_is_complete = all(row[col_index]['is_marked'] for row in board)
                return row_is_complete or column_is_complete


def day04a():
    draw_numbers, boards = get_draw_numbers_and_boards()
    for draw_number in draw_numbers:
        for board in boards:
            if bingo(board, draw_number):
                return draw_number * sum(tile['number'] for row in board for tile in row if not tile['is_marked'])


def day04b():
    draw_numbers, boards = get_draw_numbers_and_boards()
    last_draw = 0
    last_board = None
    for board in boards:
        for draw, draw_number in enumerate(draw_numbers):
            if bingo(board, draw_number):
                if draw > last_draw:
                    last_draw = draw
                    last_board = board
                break
    return draw_numbers[last_draw] * sum(tile['number'] for row in last_board for tile in row if not tile['is_marked'])


print(day04a())
print(day04b())
