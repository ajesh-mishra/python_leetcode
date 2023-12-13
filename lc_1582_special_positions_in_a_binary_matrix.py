class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        count, m, n = 0, len(mat), len(mat[0])
        for x, y in [(i, j) for i in range(m) for j in range(n)]:
            if mat[x][y] != 1:
                continue
            if (
                sum([mat[i][y] for i in range(m)]) + sum([mat[x][j] for j in range(n)])
                == 2
            ):
                count += 1

        return count


if __name__ == "__main__":
    assert Solution().numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1
    assert Solution().numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
