class Solution:
    @staticmethod
    def image_smoother(img: list[list[int]]) -> list[list[int]]:
        m = len(img)
        n = len(img[0])
        result = [[0 for _ in range(n)] for _ in range(m)]

        for i, j in [(x, y) for x in range(m) for y in range(n)]:
            neighbour_sum, count = 0, 0
            for a, b in [
                (dx, dy)
                for dx in range(i - 1, i + 2)
                for dy in range(j - 1, j + 2)
                if 0 <= dx < m and 0 <= dy < n
            ]:
                neighbour_sum += img[a][b]
                count += 1
            result[i][j] = neighbour_sum // count

        return result


if __name__ == "__main__":
    assert Solution().image_smoother(img=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert Solution().image_smoother(
        img=[[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    ) == [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
