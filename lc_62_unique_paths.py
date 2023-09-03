class Solution:
    @staticmethod
    def unique_paths(m: int, n: int) -> int:
        cache: list[list[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    cache[i][j] = 1
                    continue
                cache[i][j] = cache[i][j + 1] + cache[i + 1][j]

        return cache[0][0]


if __name__ == "__main__":
    assert Solution().unique_paths(m=3, n=2) == 3
    assert Solution().unique_paths(m=3, n=7) == 28
