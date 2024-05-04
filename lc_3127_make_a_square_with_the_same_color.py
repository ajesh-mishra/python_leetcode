class Solution:
    @staticmethod
    def can_make_square(grid: list[list[str]]) -> bool:
        def dfs(x: int, y: int, color: str) -> None:
            visited.add((x, y))
            path.append((x, y))

            for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if not (0 <= new_x < 3):
                    continue
                if not (0 <= new_y < 3):
                    continue
                if color != grid[new_x][new_y]:
                    continue
                if (new_x, new_y) in visited:
                    continue

                dfs(new_x, new_y, color)

        visited: set[tuple[int, int]] = set()

        for i, j in [(i, j) for i in range(3) for j in range(3)]:
            if (i, j) in visited:
                continue
            path: list[tuple[int, int]] = []
            dfs(i, j, grid[i][j])

            if len(path) > 3:
                return True
            if len(path) == 3:
                if len({p[0] for p in path}) != 1 and len({p[1] for p in path}) != 1:
                    return True

        return False


if __name__ == "__main__":
    assert Solution.can_make_square(
        grid=[["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]
    )
    assert not Solution.can_make_square(
        grid=[["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]
    )
    assert Solution.can_make_square(
        grid=[["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]
    )
