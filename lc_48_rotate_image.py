class Solution:
    @staticmethod
    def rotate(matrix: list[list[int]]) -> None:
        length = len(matrix)
        rotated = [[0 for _ in range(length)] for _ in range(length)]

        for j, row in enumerate(matrix):
            for i, value in enumerate(row):
                rotated[i][length - j - 1] = value

        for i, row in enumerate(rotated):
            for j, value in enumerate(row):
                matrix[i][j] = value

        # (0, 0) - (0, 3)
        # (0, 3) - (3, 3)
        # (3, 3) - (3, 0)
        # (3, 0) - (0, 0)
        # 
        # (0, 1) - (1, 3)
        # (1, 3) - (3, 2)
        # (3, 2) - (2, 0)
        # (2, 0) - (0, 1)
        #
        # (0, 2) - (2, 3)
        # (2, 3) - (3, 1)
        # (3, 1) - (2, 0)
        # (2, 0) - (0, 2)
        #
        # (0, 3) - (3, 3)


if __name__ == '__main__':
    Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
