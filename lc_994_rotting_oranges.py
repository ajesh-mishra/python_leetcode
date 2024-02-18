class Solution:
    @staticmethod
    def oranges_rotting(grid: list[list[int]]) -> int:
        time, m, n = 0, len(grid), len(grid[0])
        rotten_queue = [
            (i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 2
        ]

        def good_oranges_count() -> int:
            return len([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])

        if good_oranges_count() == 0:
            return 0

        while rotten_queue:
            x, y, t = rotten_queue.pop(0)

            for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                if not (0 <= new_x < m):
                    continue
                if not (0 <= new_y < n):
                    continue

                if grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    time = t + 1
                    rotten_queue.append((new_x, new_y, t + 1))

        if good_oranges_count() != 0:
            return -1
        else:
            return time


if __name__ == "__main__":
    assert Solution.oranges_rotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert Solution.oranges_rotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert Solution.oranges_rotting(grid=[[0, 2]]) == 0
    assert Solution.oranges_rotting(grid=[[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2
