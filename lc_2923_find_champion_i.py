class Solution:
    @staticmethod
    def find_champion(grid: list[list[int]]) -> int:
        max_points, max_index = 0, 0

        for index, player in enumerate(grid):
            point: int = int("".join([str(p) for p in player]), 2)
            if max_points < point:
                max_points = point
                max_index = index

        return max_index


if __name__ == "__main__":
    assert Solution().find_champion(grid=[[0, 1], [0, 0]]) == 0
    assert Solution().find_champion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]) == 1
