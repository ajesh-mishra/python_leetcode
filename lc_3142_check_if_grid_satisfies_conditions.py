class Solution:
    @staticmethod
    def satisfies_conditions(grid: list[list[int]]) -> bool:
        # checks if all the columns are different
        if not all(map(lambda x, y: x != y, grid[0], grid[0][1:])):
            return False

        # checks if all the elements in the row are same
        m, n = len(grid), len(grid[0])

        for j in range(n):
            if len(set([grid[i][j] for i in range(m)])) != 1:
                return False

        return True


if __name__ == "__main__":
    assert Solution.satisfies_conditions(grid=[[1, 0, 2], [1, 0, 2]])
    assert not Solution.satisfies_conditions(grid=[[1, 1, 1], [0, 0, 0]])
    assert not Solution.satisfies_conditions(grid=[[1], [2], [3]])
