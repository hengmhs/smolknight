import copy

# Constants

EMPTY = 0
PAWN = 1
KNIGHT = 2

GREEN_TEXT = "\033[32m"
RED_TEXT = "\033[31m"
TEXT_RESET = "\033[0m"
GREEN_BG = "\033[42m"


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


def move_knight(grid, target_coords, curr_coords):
    target_r, target_c = target_coords
    curr_r, curr_c = curr_coords

    if target_coords in valid_knight_moves(curr_r, curr_c) and is_valid_move(
        grid, target_r, target_c
    ):
        grid[target_r][target_c] = grid[curr_r][curr_c]
        grid[curr_r][curr_c] = 0


def move_pawns(grid):
    new_grid = copy.deepcopy(grid)
    for r_idx, row in enumerate(grid):
        for c_idx, val in enumerate(row):
            if val == PAWN:
                # check if the knight is blocking
                if new_grid[r_idx + 1][c_idx] == EMPTY:
                    new_grid[r_idx + 1][c_idx] = PAWN
                    new_grid[r_idx][c_idx] = EMPTY
    return new_grid


def is_game_over(grid):
    for val in grid[-1]:
        if val == PAWN:
            return True
    return False


def is_round_over(grid):
    for row in grid:
        for val in row:
            if val == PAWN:
                return False
    return True


# Validation Functions


def validate_level_select_input(s, level_map):
    if not s.isnumeric():
        return False
    level = int(s)
    if level not in level_map:
        return False
    return True


def is_valid_move(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


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


# Display Functions
def display_intro():
    print(
        """
▄▖     ▜ ▌   ▘  ▌ ▗ 
▚ ▛▛▌▛▌▐ ▙▘▛▌▌▛▌▛▌▜▘
▄▌▌▌▌▙▌▐▖▛▖▌▌▌▙▌▌▌▐▖
              ▄▌    
    """
    )
    # Introduction
    print("┌───┐")
    print("RULES")
    print("└───┘")

    print(
        "1. Use your knight to stop the pawns from reaching your backline (the 8th row)"
    )
    print(
        "2. After you move, all enemy pawns will move forward unless there is a pawn or knight blocking it"
    )
    print("3. Enemy pawns will not capture your knight.")
    print(
        "4. All enemy pawns in row 1 will move first, then row 2, and so on. If there is a pawn in row A1 and A2, the pawn in A1 will be blocked from moving by the pawn in A2. \n"
    )


def display_levels(level_map):
    print("Levels: ")

    for level_num, level_data in level_map.items():
        print(f"{level_num}. {level_data["title"]}")

    print("\n")


def display_end_game_screen():
    print(GREEN_TEXT)
    print("┌─────────────────┐")
    print("ALL LEVELS COMPLETE")
    print("└─────────────────┘")
    print(TEXT_RESET)
    print("You've completed the game! Congratulations!\n")
    print("Thank for playing Smolknight :D")


def display_round_success():
    print(GREEN_TEXT)
    print("┌───────────┐")
    print("ROUND SUCCESS")
    print("└───────────┘")
    print(TEXT_RESET)


def display_round_failure():
    print(RED_TEXT)
    print("┌───────┐")
    print("GAME OVER")
    print("└───────┘")
    print(TEXT_RESET)
    print("A pawn reached your backline!\n")


def display_char(v):
    char_map = {
        EMPTY: ".",
        PAWN: f"{RED_TEXT}♟{TEXT_RESET}",
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
                highlight_start = GREEN_BG
                highlight_end = TEXT_RESET
            print(highlight_start + display_char(val) + highlight_end, end=" ")
        print(str(r_idx + 1) + "  ", end=end_c)
    print("   A B C D E F G H")


def main():

    curr_grid = []

    display_intro()

    level_map = {
        0: {
            "title": "Lone Star",
            "grid": [
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (4, 4),
        },
        1: {
            "title": "Gemini",
            "grid": [
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (4, 4),
        },
        2: {
            "title": "Conga Line",
            "grid": [
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (7, 7),
        },
        3: {
            "title": "Birds of a Feather",
            "grid": [
                [0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (7, 0),
        },
        4: {
            "title": "Wall Climber",
            "grid": [
                [0, 0, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (7, 4),
        },
        5: {
            "title": "Christmas Present",
            "grid": [
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (6, 6),
        },
        6: {
            "title": "Parallel Lives",
            "grid": [
                [1, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (0, 4),
        },
        7: {
            "title": "Mercy",
            "grid": [
                [0, 1, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (0, 6),
        },
        8: {
            "title": "False Flag",
            "grid": [
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (7, 4),
        },
        9: {
            "title": "Ambush",
            "grid": [
                [0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (1, 4),
        },
        10: {
            "title": "Free Will",
            "grid": [
                [0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (7, 7),
        },
        11: {
            "title": "Vendetta",
            "grid": [
                [0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (5, 3),
        },
        12: {
            "title": "Regiment",
            "grid": [
                [0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (5, 3),
        },
        13: {
            "title": "Forefathers",
            "grid": [
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (3, 3),
        },
        14: {
            "title": "Cascade",
            "grid": [
                [0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (7, 1),
        },
        15: {
            "title": "Slice",
            "grid": [
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "knight_pos": (0, 5),
        },
    }

    display_levels(level_map)

    level_select = input("Level Select: ")

    while not validate_level_select_input(level_select, level_map):
        print(f"{RED_TEXT}{level_select} is not a valid level.{TEXT_RESET}")
        level_select = input("Level Select: ")

    level = int(level_select)

    level_map_instance = copy.deepcopy(level_map)

    while True:
        # end of game check
        if level >= len(level_map):
            display_end_game_screen()
            break

        curr_level = level_map_instance[level]

        if is_round_over(curr_grid):
            print(f"Level {level}: {curr_level["title"]}\n")

            # set up the next level
            curr_grid = curr_level["grid"]
            curr_knight_pos = curr_level["knight_pos"]
            curr_grid[curr_knight_pos[0]][curr_knight_pos[1]] = KNIGHT

        # display board state
        valid_knight_moves_res = valid_knight_moves(
            curr_knight_pos[0], curr_knight_pos[1]
        )
        draw_grid(curr_grid, valid_knight_moves_res)

        print("Type rs to reset the level, q to quit\n")
        target_move = input("Move: ")

        # quit the game
        if target_move == "q":
            exit()

        # reset the current level
        if target_move == "rs":
            print(f"{GREEN_TEXT}Level reset{TEXT_RESET}")
            level_map_instance = copy.deepcopy(level_map)
            curr_level = level_map_instance[level]
            curr_grid = curr_level["grid"]
            curr_knight_pos = curr_level["knight_pos"]
            curr_grid[curr_knight_pos[0]][curr_knight_pos[1]] = KNIGHT
            continue

        try:
            target_coords = convert_to_coords(target_move)
            if target_coords in valid_knight_moves_res:
                move_knight(curr_grid, target_coords, curr_knight_pos)
                curr_knight_pos = target_coords
                curr_grid = move_pawns(curr_grid)
                if is_round_over(curr_grid):
                    display_round_success()
                    level += 1
                elif is_game_over(curr_grid):
                    display_round_failure()
                    draw_grid(curr_grid, [])
                    break
            else:
                print(f"{RED_TEXT}{target_move} is an invalid move{TEXT_RESET}")
        except:
            # use with caution as this masks other types of errors as an input error
            print(f"{RED_TEXT}{target_move} is an invalid move{TEXT_RESET}")


if __name__ == "__main__":
    main()
