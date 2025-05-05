import copy

grid = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

EMPTY = 0
PAWN = 1
KNIGHT = 2


def convert_to_coords(s):
    c_map = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
    }

    # A2
    # column, then row
    # convert to row, column
    # (1, 0)

    return (int(s[1]) - 1, c_map[s[0].lower()])


def display_char(v):
    char_map = {
        EMPTY: ".",
        PAWN: "\033[31m♟\033[0m",
        KNIGHT: "♞",
    }

    return char_map[v]


def draw_grid(grid, valid_knight_moves_res):
    print("   A B C D E F G H")
    for r_idx, row in enumerate(grid):
        print(str(r_idx + 1) + "  ", end="")
        for c_idx, val in enumerate(row):
            end_c = " "
            highlight_start = ""
            highlight_end = ""
            if c_idx == len(row) - 1:
                end_c = "\n"
            if (r_idx, c_idx) in valid_knight_moves_res:
                highlight_start = "\033[42m"
                highlight_end = "\033[0m"
            print(highlight_start + display_char(val) + highlight_end, end=" ")
        print(str(r_idx + 1) + "  ", end=end_c)
    print("   A B C D E F G H")


def is_valid_move(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c <= len(grid[0])


def move_knight(grid, target_coords, curr_coords):
    target_r, target_c = target_coords
    curr_r, curr_c = curr_coords

    if target_coords in valid_knight_moves(curr_r, curr_c) and is_valid_move(
        grid, target_r, target_c
    ):
        grid[target_r][target_c] = grid[curr_r][curr_c]
        print(grid[curr_r][curr_c])
        grid[curr_r][curr_c] = 0
    else:
        print("Invalid Move")


def valid_knight_moves(start_r, start_c):
    directions = [
        [-1, -2],
        [-2, -1],
        [-2, 1],
        [-1, 2],
        [1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
    ]
    valid_dirs = []
    # . x . x .
    # x . . . x
    # . . K . .
    # x . . . x
    # . x . x .
    for mov_r, mov_c in directions:
        end_r = start_r + mov_r
        end_c = start_c + mov_c
        valid_dirs.append((end_r, end_c))
    return valid_dirs


# spawn the knight
knight_pos = (3, 4)
grid[knight_pos[0]][knight_pos[1]] = KNIGHT


def move_pawns(grid):
    new_grid = copy.deepcopy(grid)
    for r_idx, row in enumerate(grid):
        for c_idx, val in enumerate(row):
            if val == PAWN:
                print(r_idx, c_idx)
                # check if the knight is blocking
                if new_grid[r_idx + 1][c_idx] == EMPTY:
                    new_grid[r_idx + 1][c_idx] = PAWN
                    new_grid[r_idx][c_idx] = EMPTY
    return new_grid


while True:
    valid_knight_moves_res = valid_knight_moves(knight_pos[0], knight_pos[1])
    draw_grid(grid, valid_knight_moves_res)

    target_move = input("Move: ")
    try:
        target_coords = convert_to_coords(target_move)
        if target_coords in valid_knight_moves_res:
            move_knight(grid, target_coords, knight_pos)
            knight_pos = target_coords
            grid = move_pawns(grid)
        else:
            print(f"{target_move} is an invalid move")
    except:
        # use with caution as this masks other types of errors as an input error
        print(f"{target_move} is an invalid move")
