class Solution:
    @staticmethod
    def get_maximum_gold(grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])

        def dfs(x: int, y: int, gold: int) -> None:
            nonlocal max_gold
            gold += grid[x][y]
            visited.add((x, y))

            for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if not (0 <= new_x < m):
                    continue
                if not (0 <= new_y < n):
                    continue
                if (new_x, new_y) in visited:
                    continue
                if grid[new_x][new_y] == 0:
                    continue

                dfs(new_x, new_y, gold)
                visited.remove((new_x, new_y))

            max_gold = max(max_gold, gold)

        max_gold: int = 0

        for i, j in [(i, j) for i in range(m) for j in range(n) if grid[i][j] != 0]:
            visited: set[tuple[int, int]] = set()
            dfs(i, j, 0)

        return max_gold


if __name__ == "__main__":
    print(Solution.get_maximum_gold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
    assert Solution.get_maximum_gold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]) == 24
    assert (
        Solution.get_maximum_gold(
            grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        )
        == 28
    )
    assert (
        Solution.get_maximum_gold(
            [
                [1, 0, 7, 0, 0, 0],
                [2, 0, 6, 0, 1, 0],
                [3, 5, 6, 7, 4, 2],
                [4, 3, 1, 0, 2, 0],
                [3, 0, 5, 0, 20, 0],
            ]
        )
        == 60
    )
