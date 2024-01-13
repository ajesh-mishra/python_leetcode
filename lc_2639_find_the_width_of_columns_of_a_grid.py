class Solution:
    def find_column_width(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        return [max([len(str(grid[i][j])) for i in range(m)]) for j in range(n)]


if __name__ == "__main__":
    assert Solution().find_column_width(grid=[[1], [22], [333]]) == [3]
    assert Solution().find_column_width(
        grid=[[-15, 1, 3], [15, 7, 12], [5, 6, -2]]
    ) == [
        3,
        1,
        2,
    ]
