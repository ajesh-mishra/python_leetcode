class Solution:
    @staticmethod
    def transpose(mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        new_matrix: list[list[int]] = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = mat[i][j]

        return new_matrix

    @staticmethod
    def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        if m > n:
            mat = Solution.transpose(matrix)
            m, n = n, m
        else:
            mat = matrix

        for delta_y in range(-n, n + 1):
            current_diagonal: set[int] = set()

            for x, y in [(i, i) for i in range(m)]:
                if not (0 <= x < m and 0 <= y + delta_y < n):
                    continue
                current_diagonal.add(mat[x][y + delta_y])

            if len(current_diagonal) > 1:
                return False

        return True


if __name__ == "__main__":
    assert Solution.is_toeplitz_matrix(
        matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    )
    assert not Solution.is_toeplitz_matrix(matrix=[[1, 2], [2, 2]])
    assert not Solution.is_toeplitz_matrix(
        matrix=[[41, 45], [81, 41], [73, 81], [47, 73], [0, 47], [79, 76]]
    )
