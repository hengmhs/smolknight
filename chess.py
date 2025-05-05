grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


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

    # E4
    # column, then row
    # convert to row, column

    return (int(s[1]), c_map[s[0].lower()])


def draw_grid(grid):

    # for row in grid:
    #     for val in row:
    #         print("┌───┐", end="")
    #     print("\n")
    #     for val in row:
    #         print("│ " + str(val) + " │", end="")
    #     print("\n")
    #     for val in row:
    #         print("└───┘", end="")
    #     print("\n")
    print("   A B C D E F G H")
    for idx, row in enumerate(grid):
        print(str(idx + 1) + "  ", end="")
        for c_idx, val in enumerate(row):
            end_c = " "
            if c_idx == len(row) - 1:
                end_c = "\n"
            print(str("."), end=end_c)


draw_grid(grid)
