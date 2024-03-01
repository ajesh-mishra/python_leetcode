from collections import deque
from typing import Deque


class Solution:
    @staticmethod
    def is_bipartite(graph: list[list[int]]) -> bool:
        def dfs(i: int) -> bool:
            for neighbour in graph[i]:
                if color[neighbour] == color[i]:
                    return False
                if color[neighbour] is None:
                    color[neighbour] = not color[i]
                    if not dfs(neighbour):
                        return False

            return True

        color: list[bool | None] = [None for _ in range(len(graph))]

        for index, c in enumerate(color):
            if c is not None:
                continue

            color[index] = True

            if not dfs(index):
                return False

        return True

    @staticmethod
    def is_bipartite_bfs(graph: list[list[int]]) -> bool:
        def inner(i: int) -> bool:
            queue: Deque[int] = deque([i])
            color[i] = True

            while queue:
                node = queue.popleft()

                for neighbour in graph[node]:
                    if color[neighbour] == color[node]:
                        return False
                    if color[neighbour] is None:
                        color[neighbour] = not color[node]
                        queue.append(neighbour)

            return True

        color: list[bool | None] = [None for _ in range(len(graph))]
        return all([inner(index) for index, c in enumerate(color) if c is None])


if __name__ == "__main__":
    assert Solution.is_bipartite(
        graph=[
            [3, 4, 6],  # 0
            [3, 6],  # 1
            [3, 6],  # 2
            [0, 1, 2, 5],  # 3
            [0, 7, 8],  # 4
            [3],  # 5
            [0, 1, 2, 7],  # 6
            [4, 6],  # 7
            [4],  # 8
            [],  # 9
        ]
    )
    assert Solution.is_bipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]])
    assert not Solution.is_bipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert not Solution.is_bipartite(
        graph=[
            [2, 4],
            [2, 3, 4],
            [0, 1],
            [1],
            [0, 1],
            [7],
            [9],
            [5],
            [],
            [6],
            [12, 14],
            [],
            [10],
            [],
            [10],
            [19],
            [18],
            [],
            [16],
            [15],
            [23],
            [23],
            [],
            [20, 21],
            [],
            [],
            [27],
            [26],
            [],
            [],
            [34],
            [33, 34],
            [],
            [31],
            [30, 31],
            [38, 39],
            [37, 38, 39],
            [36],
            [35, 36],
            [35, 36],
            [43],
            [],
            [],
            [40],
            [],
            [49],
            [47, 48, 49],
            [46, 48, 49],
            [46, 47, 49],
            [45, 46, 47, 48],
        ]
    )
    assert not Solution.is_bipartite(
        graph=[
            [],
            [2, 4, 6],
            [1, 4, 8, 9],
            [7, 8],
            [1, 2, 8, 9],
            [6, 9],
            [1, 5, 7, 8, 9],
            [3, 6, 9],
            [2, 3, 4, 6, 9],
            [2, 4, 5, 6, 7, 8],
        ]
    )
