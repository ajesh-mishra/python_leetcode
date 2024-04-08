class Solution:
    @staticmethod
    def count_distinct_islands(grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited: list[list[int]] = [[False for _ in range(n)] for _ in range(m)]
        distinct_island: set[tuple[tuple[int, int], ...]] = set()

        def dfs(
            a: int, b: int, base_i: int, base_j: int, island: list[tuple[int, int]]
        ):
            if visited[a][b]:
                return

            visited[a][b] = True
            island.append((a, b))

            for new_a, new_b in [(a - 1, b), (a, b - 1), (a + 1, b), (a, b + 1)]:
                if not (0 <= new_a < m) or not (0 <= new_b < n):
                    continue

                if grid[new_a][new_b] != 1:
                    continue

                dfs(new_a, new_b, base_i, base_j, island)

            return island

        for i, j in [(x, y) for x in range(m) for y in range(n)]:
            if visited[i][j] or grid[i][j] != 1:
                continue

            complete_island = dfs(i, j, i, j, [])
            distinct_island.add(tuple((x1 - i, y1 - j) for x1, y1 in complete_island))

        return len(distinct_island)


if __name__ == "__main__":
    assert (
        Solution.count_distinct_islands(
            [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
        )
        == 1
    )

    assert (
        Solution.count_distinct_islands(
            [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
        )
        == 3
    )
