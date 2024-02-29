class Solution:
    @staticmethod
    def solve(board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(a: int, b: int, path: set[tuple[int, int]]) -> set[tuple[int, int]]:
            nonlocal should_update

            if not 0 <= a < m - 1:
                should_update = False

            if not 0 <= b < n - 1:
                should_update = False

            path.add((a, b))

            for new_a, new_b in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
                if not 0 <= new_a < m:
                    should_update = False
                    continue

                if not 0 <= new_b < n:
                    should_update = False
                    continue

                if (new_a, new_b) not in path and board[new_a][new_b] == "O":
                    dfs(new_a, new_b, path)

            return path

        visited: set[tuple[int, int]] = set()

        for x, y in [(i, j) for i in range(m) for j in range(n)]:
            if board[x][y] != "O" or (x, y) in visited:
                continue

            should_update = True
            p = dfs(x, y, set())
            visited |= p

            if not should_update:
                continue

            for i, j in p:
                board[i][j] = "X"


if __name__ == "__main__":
    assert Solution.solve(
        board=[
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    ) == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
