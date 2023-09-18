class Solution:
    @staticmethod
    def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
        strength_mat: list[(int, int)] = [
            (index, len([num for num in row if num == 1]))
            for index, row in enumerate(mat)
        ]
        strength_mat.sort(key=lambda x: x[1])
        return [num for num, _ in strength_mat[:k]]


if __name__ == "__main__":
    assert Solution().k_weakest_rows(
        mat=[
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        k=3,
    ) == [2, 0, 3]
    assert Solution().k_weakest_rows(
        mat=[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], k=2
    ) == [0, 2]
