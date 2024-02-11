class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])

        answer: list[list[int | None]] = [
            [matrix[i][j] for j in range(n)] for i in range(m)
        ]

        for column in range(n):
            col_max = 0
            minus_ones = []

            for row in range(m):
                if answer[row][column] == -1:
                    minus_ones.append(row)
                col_max = max(col_max, answer[row][column])

            for minus_one in minus_ones:
                answer[minus_one][column] = col_max

        return answer
