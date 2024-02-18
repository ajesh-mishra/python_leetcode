class Solution:
    @staticmethod
    def odd_cells(m: int, n: int, indices: list[list[int]]) -> int:
        row_count: list[int] = [0 for _ in range(m)]
        col_count: list[int] = [0 for _ in range(n)]

        for i, j in indices:
            row_count[i] += 1
            col_count[j] += 1

        result: list[list[int]] = [[count for _ in range(n)] for count in row_count]
        odd_count = 0

        for j, count in enumerate(col_count):
            for i in range(m):
                if (result[i][j] + count) % 2 != 0:
                    odd_count += 1

        return odd_count


if __name__ == "__main__":
    assert Solution.odd_cells(m=2, n=3, indices=[[0, 1], [1, 1]]) == 6
    assert Solution.odd_cells(m=2, n=2, indices=[[1, 1], [0, 0]]) == 0
