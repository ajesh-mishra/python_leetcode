class Solution:
    @staticmethod
    def ones_minus_zeros(grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        result = [[0 for _ in range(n)] for _ in range(m)]

        for x, y in [(x, y) for x in range(m) for y in range(n)]:
            ones_col = "".join([str(grid[i][y]) for i in range(m)]).count("1")
            zeros_col = m - ones_col
            ones_row = "".join([str(grid[x][j]) for j in range(n)]).count("1")
            zeros_row = n - ones_row
            result[x][y] = ones_row + ones_col - zeros_row - zeros_col

        return result


if __name__ == "__main__":
    assert Solution().ones_minus_zeros(grid=[[0, 1, 1], [1, 0, 1], [0, 0, 1]]) == [
        [0, 0, 4],
        [0, 0, 4],
        [-2, -2, 2],
    ]
    assert Solution().ones_minus_zeros(grid=[[1, 1, 1], [1, 1, 1]]) == [
        [5, 5, 5],
        [5, 5, 5],
    ]
