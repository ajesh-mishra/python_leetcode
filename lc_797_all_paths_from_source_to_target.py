class Solution:
    @staticmethod
    def all_paths_source_target(graph: list[list[int]]) -> list[list[int]]:
        def dfs(source: int, path: list[int]) -> None:
            if source == target:
                paths.append(path)
                return None

            for neighbour in graph[source]:
                dfs(neighbour, path + [neighbour])

        target = max([node for row in graph for node in row])
        paths: list[list[int]] = []

        dfs(0, [0])
        return paths


if __name__ == "__main__":
    assert Solution().all_paths_source_target(graph=[[1, 2], [3], [3], []]) == [
        [0, 1, 3],
        [0, 2, 3],
    ]
    assert Solution().all_paths_source_target(
        graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]
    ) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
