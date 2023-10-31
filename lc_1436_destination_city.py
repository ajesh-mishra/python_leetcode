class Solution:
    @staticmethod
    def dest_city(paths: list[list[str]]) -> str:
        sources: set[str] = {path[0] for path in paths}
        destinations: set[str] = {path[1] for path in paths}
        return list(destinations.difference(sources))[0]


if __name__ == "__main__":
    assert (
        Solution().dest_city(
            paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        )
        == "Sao Paulo"
    )
    assert Solution().dest_city(paths=[["B", "C"], ["D", "B"], ["C", "A"]]) == "A"
    assert Solution().dest_city(paths=[["A", "Z"]]) == "Z"
