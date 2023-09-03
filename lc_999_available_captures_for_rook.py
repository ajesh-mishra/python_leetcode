from typing import Literal, Type

MOVE: Type[str] = Literal["up", "down", "left", "right"]


class Solution:
    @staticmethod
    def move(board: list[list[str]], moves: range, pos: int, to_move: MOVE) -> int:
        count = 0
        for move in moves:
            if to_move == "up" or to_move == "down":
                value = board[move][pos]
            else:
                value = board[pos][move]

            if value == "B":
                break
            if value == "p":
                count += 1
                break
        return count

    @staticmethod
    def num_rook_captures(board: list[list[str]]) -> int:
        count = 0

        row, col = [
            (r, c)
            for r, line in enumerate(board)
            for c, value in enumerate(line)
            if value == "R"
        ][0]

        count += Solution().move(board, range(row, -1, -1), col, "up")
        count += Solution().move(board, range(row, 8, 1), col, "down")
        count += Solution().move(board, range(col, -1, -1), row, "left")
        count += Solution().move(board, range(col, 8, 1), row, "right")

        return count


if __name__ == "__main__":
    assert (
        Solution().num_rook_captures(
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", "R", ".", ".", ".", "p"],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
            ]
        )
        == 3
    )

    assert (
        Solution().num_rook_captures(
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", "p", "p", "p", "p", "p", ".", "."],
                [".", "p", "p", "B", "p", "p", ".", "."],
                [".", "p", "B", "R", "B", "p", ".", "."],
                [".", "p", "p", "B", "p", "p", ".", "."],
                [".", "p", "p", "p", "p", "p", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
            ]
        )
        == 0
    )

    assert (
        Solution().num_rook_captures(
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                ["p", "p", ".", "R", ".", "p", "B", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
            ]
        )
        == 3
    )

    assert (
        Solution().num_rook_captures(
            [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "R", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
            ]
        )
        == 0
    )
