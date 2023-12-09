import copy


class Solution:
    @staticmethod
    def are_similar(mat: list[list[int]], k: int) -> bool:
        mat_1 = copy.deepcopy(mat)

        for _ in range(k):
            for index, row in enumerate(mat_1):
                if index % 2 == 0:
                    last = row.pop()
                    row.insert(0, last)
                    mat_1[index] = row
                else:
                    first = row.pop(0)
                    row.append(first)
                    mat_1[index] = row

        return mat == mat_1


if __name__ == "__main__":
    assert Solution().are_similar(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2)
    assert Solution().are_similar(mat=[[2, 2], [2, 2]], k=3)
    assert not Solution().are_similar(mat=[[1, 2]], k=1)
