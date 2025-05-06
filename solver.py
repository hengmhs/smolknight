import chess, copy

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
    valid_knight_moves_res = chess.valid_knight_moves(knight_pos[0], knight_pos[1])
    for target_coords in valid_knight_moves_res:
        grid_copy = copy.deepcopy(grid)
        if not chess.is_valid_move(grid_copy, target_coords[0], target_coords[1]):
            continue
        chess.move_knight(grid_copy, target_coords, knight_pos)
        grid_copy = chess.move_pawns(grid_copy)
        if chess.is_round_over(grid_copy):
            res.append(target_coords)
        elif chess.is_game_over(grid_copy):
            continue
    return res


def print_solution(ans_arr):
    print("-----------")
    print(f"Solution Found!")
    print("-----------")
    for r, c in ans_arr:
        print(convert_idx_to_notation(r, c))
    print("\n")


def recursive_solve(grid, knight_pos):
    res = []

    def solve(grid, knight_pos, ans_arr, depth):
        print("checking knight pos: ", knight_pos)
        print("current steps: ", ans_arr)
        print("depth: ", depth)

        is_round_over = chess.is_round_over(grid)
        is_game_over = chess.is_game_over(grid)

        # base case
        if is_round_over:
            res.append(ans_arr)
            print("ans: ", ans_arr)
            print_solution(ans_arr)
            exit()
            return
        elif is_game_over:
            return

        valid_knight_moves_res = chess.valid_knight_moves(knight_pos[0], knight_pos[1])
        for new_knight_coords in valid_knight_moves_res:
            grid_copy = copy.deepcopy(grid)
            if not chess.is_valid_move(
                grid_copy, new_knight_coords[0], new_knight_coords[1]
            ):
                continue
            chess.move_knight(grid_copy, new_knight_coords, knight_pos)
            grid_copy = chess.move_pawns(grid_copy)
            ans_arr_copy = ans_arr.copy()
            ans_arr_copy.append((new_knight_coords))
            solve(grid_copy, new_knight_coords, ans_arr_copy, depth + 1)

    solve(grid, knight_pos, [], 0)
    return res


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
