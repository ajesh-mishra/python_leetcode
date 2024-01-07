import math


class Solution:
    def area_of_max_diagonal(self, dimensions: list[list[int]]) -> int:
        diagonal_and_area = [(math.sqrt(x * x + y * y), x * y) for x, y in dimensions]
        diagonal_and_area.sort(key=lambda x: (x[0], x[1]), reverse=True)
        return diagonal_and_area[0][1]


if __name__ == "__main__":
    assert Solution().area_of_max_diagonal(dimensions=[[9, 3], [8, 6]]) == 48
    assert Solution().area_of_max_diagonal(dimensions=[[3, 4], [4, 3]]) == 12
