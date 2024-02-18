class Solution:
    @staticmethod
    def flood_fill(
        image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        if (original_color := image[sr][sc]) == color:
            return image

        def dfs(r, c) -> None:
            if not (0 <= r < m):
                return None
            if not (0 <= c < n):
                return None

            image[r][c] = color

            for new_r, new_c in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                try:
                    if image[new_r][new_c] == original_color:
                        dfs(new_r, new_c)
                except IndexError:
                    continue

        m, n = len(image), len(image[0])
        dfs(sr, sc)

        return image


if __name__ == "__main__":
    assert Solution.flood_fill(
        image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2
    ) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert Solution.flood_fill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0) == [
        [0, 0, 0],
        [0, 0, 0],
    ]
