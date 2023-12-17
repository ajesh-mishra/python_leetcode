class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        set_grid, result = set(), []

        for row in grid:
            for element in row:
                if element in set_grid:
                    result.append(element)
                set_grid.add(element)

        x = list(
            filter(lambda x: x not in set_grid, range(1, len(grid) * len(grid[0]) + 1))
        )[0]

        result.append(x)
        return result


if __name__ == "__main__":
    assert Solution().findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]]) == [2, 4]
    assert Solution().findMissingAndRepeatedValues(
        grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    ) == [9, 5]
