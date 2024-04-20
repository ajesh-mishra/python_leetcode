class Solution:
    @staticmethod
    def find_farmland(land: list[list[int]]) -> list[list[int]]:
        m: int = len(land)
        n: int = len(land[0])

        def dfs(i: int, j: int) -> None:
            visited.add((i, j))

            if i < group[0]:
                group[0], group[1] = i, j
            if i == group[0] and j < group[1]:
                group[0], group[1] = i, j
            if i >= group[2]:
                group[2], group[3] = i, j

            for (
                new_i,
                new_j,
            ) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= new_i < m) or not (0 <= new_j < n):
                    continue
                if land[new_i][new_j] != 1:
                    continue
                if (new_i, new_j) in visited:
                    continue
                dfs(new_i, new_j)

        visited: set[tuple[int, int]] = set()
        result: list[list[int]] = []

        for x, y in [(x, y) for x in range(m) for y in range(n)]:
            if land[x][y] == 0 or (x, y) in visited:
                continue
            group = [m - 1, n - 1, 0, 0]
            dfs(x, y)
            result.append(group)

        return result


if __name__ == "__main__":
    assert Solution.find_farmland(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [
        [0, 0, 0, 0],
        [1, 1, 2, 2],
    ]
    assert Solution.find_farmland(land=[[1, 1], [1, 1]]) == [[0, 0, 1, 1]]
    assert Solution.find_farmland(land=[[0]]) == []
