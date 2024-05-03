from collections import defaultdict
from functools import cache
from typing import DefaultDict


class Solution:
    @staticmethod
    def sum_of_distances_in_tree(n: int, edges: list[list[int]]) -> list[int]:
        adjacency_list: DefaultDict[int, list[int]] = defaultdict(list)

        for x, y in edges:
            adjacency_list[x].append(y)
            adjacency_list[y].append(x)

        @cache
        def dfs(parent, child):
            total, count = 0, 1

            for neighbor in adjacency_list[child]:
                if neighbor == parent:
                    continue

                t, c = dfs(child, neighbor)
                total += t + c
                count += c

            return total, count

        return [dfs(-1, i)[0] for i in range(n)]


if __name__ == "__main__":
    assert Solution.sum_of_distances_in_tree(
        n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    ) == [8, 12, 6, 10, 10, 10]
    assert Solution.sum_of_distances_in_tree(n=1, edges=[]) == [0]
    assert Solution.sum_of_distances_in_tree(n=2, edges=[[1, 0]]) == [1, 1]
