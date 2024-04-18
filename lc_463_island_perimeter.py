class Solution:
    @staticmethod
    def island_perimeter(grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        perimeter: int = 0

        def dfs(x, y):
            nonlocal perimeter
            count: int = 0
            visited.add((x, y))

            for new_x, new_y in [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
            ]:
                if not (0 <= new_x < m) or not (0 <= new_y < n):
                    continue
                if grid[new_x][new_y] == 0:
                    continue

                count += 1

                if (new_x, new_y) not in visited:
                    dfs(new_x, new_y)

            perimeter += 4 - count

        visited: set[tuple[int, int]] = set()

        for i, j in [(i, j) for i in range(m) for j in range(n)]:
            if grid[i][j] == 1:
                dfs(i, j)
                break

        return perimeter


if __name__ == "__main__":
    assert (
        Solution.island_perimeter(
            grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        )
        == 16
    )
    assert Solution.island_perimeter(grid=[[1]]) == 4
    assert Solution.island_perimeter(grid=[[1, 0]]) == 4
