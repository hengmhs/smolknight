import chess, copy

grid = (
    [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
)
knight_pos = (2, 4)

# let's try and solve one step first


def solve(grid, knight_pos):
    res = []
    valid_knight_moves_res = chess.valid_knight_moves(knight_pos[0], knight_pos[1])
    for target_coords in valid_knight_moves_res and chess.is_valid_move(
        grid, target_coords[0], target_coords[1]
    ):
        board = copy.deepcopy(grid)
        chess.move_knight(board, target_coords, knight_pos)
        knight_pos = target_coords
        grid = chess.move_pawns(board)
        if chess.is_round_over(board):
            res.append(target_coords)
        elif chess.is_game_over(board):
            continue
    return res


print(solve(grid, knight_pos))
