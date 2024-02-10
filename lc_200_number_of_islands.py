class Solution:
    @staticmethod
    def num_islands(grid: list[list[str]]) -> int:
        def dfs(a, b):
            if not (0 <= a < i):
                return None
            if not (0 <= b < j):
                return None
            if grid[a][b] != "1":
                return None

            visited.add((a, b))

            for new_a, new_b in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
                if (new_a, new_b) not in visited:
                    dfs(new_a, new_b)

        i: int = len(grid)
        j: int = len(grid[0])
        islands: int = 0
        visited: set[tuple[int, int]] = set()

        for x, y in [(x, y) for x in range(i) for y in range(j)]:
            if (x, y) in visited or grid[x][y] == "0":
                continue
            dfs(x, y)
            islands += 1

        return islands


if __name__ == "__main__":
    assert (
        Solution().num_islands(
            grid=[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        Solution().num_islands(
            grid=[
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
