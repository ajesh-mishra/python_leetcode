class Solution:
    @staticmethod
    def maximal_network_rank(n: int, roads: list[list[int]]) -> int:
        paths = [0 for _ in range(n)]
        direct = [[0 for _ in range(n)] for _ in range(n)]

        for r1, r2 in roads:
            paths[r1] += 1
            paths[r2] += 1
            direct[r1][r2] = 1
            direct[r2][r1] = 1

        network_rank = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                network_rank = max([network_rank, paths[i] + paths[j] - direct[i][j]])

        return network_rank


if __name__ == "__main__":
    assert (
        Solution().maximal_network_rank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]])
        == 4
    )
    assert (
        Solution().maximal_network_rank(
            n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
        )
        == 5
    )
    assert (
        Solution().maximal_network_rank(
            n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        )
        == 5
    )
