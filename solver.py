import game, copy

grid = [
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
knight_pos = (0, 5)
grid[knight_pos[0]][knight_pos[1]] = 2


def solve_one_step(grid, knight_pos):
    res = []
    valid_knight_moves_res = game.valid_knight_moves(knight_pos[0], knight_pos[1])
    for target_coords in valid_knight_moves_res:
        grid_copy = copy.deepcopy(grid)
        if not game.is_valid_move(grid_copy, target_coords[0], target_coords[1]):
            continue
        game.move_knight(grid_copy, target_coords, knight_pos)
        grid_copy = game.move_pawns(grid_copy)
        if game.is_round_over(grid_copy):
            res.append(target_coords)
        elif game.is_game_over(grid_copy):
            continue
    return res


def print_solution(ans_arr):
    print("-----------")
    print(f"Solution Found!")
    print("-----------")
    for r, c in ans_arr:
        print(convert_idx_to_notation(r, c))
    print("\n")


# a DFS solver
def recursive_solve(grid, knight_pos):
    def solve(grid, knight_pos, ans_arr, depth):
        print("checking knight pos: ", knight_pos)
        print("current steps: ", ans_arr)
        print("depth: ", depth)

        is_round_over = game.is_round_over(grid)
        is_game_over = game.is_game_over(grid)

        # base case
        if is_round_over:
            print_solution(ans_arr)
            exit()
            return
        elif is_game_over:
            return

        valid_knight_moves_res = game.valid_knight_moves(knight_pos[0], knight_pos[1])
        for new_knight_coords in valid_knight_moves_res:
            grid_copy = copy.deepcopy(grid)
            if not game.is_valid_move(
                grid_copy, new_knight_coords[0], new_knight_coords[1]
            ):
                continue
            game.move_knight(grid_copy, new_knight_coords, knight_pos)
            grid_copy = game.move_pawns(grid_copy)
            ans_arr_copy = ans_arr.copy()
            ans_arr_copy.append((new_knight_coords))
            solve(grid_copy, new_knight_coords, ans_arr_copy, depth + 1)

    solve(grid, knight_pos, [], 0)


def convert_idx_to_notation(r_idx, c_idx):
    letters = "ABCDEFGH"

    return f"{letters[c_idx]}{r_idx + 1}"


for index, solution in enumerate(recursive_solve(grid, knight_pos)):
    print("-----------")
    print(f"Solution {str(index)}")
    print("-----------")
    for r, c in solution:
        print(convert_idx_to_notation(r, c))
    print("\n")


# Solutions

# Parallel Lives Solution

# F3
# H2
# G4
# E5
# C6
# A7
# B5
# A7

# False Flag Solution

# D6
# E4
# D6
# E4
# F6
# D7
# E5
# D7
# B6
# D7
# B6
# D7
