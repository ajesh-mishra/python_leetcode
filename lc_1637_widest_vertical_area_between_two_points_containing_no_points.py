class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points = sorted([point[0] for point in points])
        return max([abs(points[i] - points[i + 1]) for i in range(len(points) - 1)])


if __name__ == "__main__":
    assert (
        Solution().maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]) == 1
    )
    assert (
        Solution().maxWidthOfVerticalArea(
            points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
        )
        == 3
    )
