class Solution:
    def is_path_crossing(self, path: str) -> bool:
        points: list[tuple[int, int]] = [(0, 0)]

        for p in path:
            if p == "N":
                new_point = (points[-1][0], points[-1][1] + 1)
            elif p == "S":
                new_point = (points[-1][0], points[-1][1] - 1)
            elif p == "E":
                new_point = (points[-1][0] - 1, points[-1][1])
            else:
                new_point = (points[-1][0] + 1, points[-1][1])

            if new_point in points:
                return True

            points.append(new_point)

        return False

        # return len(points) != len(set(points))


if __name__ == "__main__":
    assert not Solution().is_path_crossing(path="NES")
    assert Solution().is_path_crossing(path="NESWW")
