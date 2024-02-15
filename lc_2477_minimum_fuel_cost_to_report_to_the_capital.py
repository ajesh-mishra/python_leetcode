import math
from collections import defaultdict
from typing import DefaultDict


class Solution:
    fuel: int

    @staticmethod
    def minimum_fuel_cost(roads: list[list[int]], seats: int) -> int:
        adjacency_list: DefaultDict[int, list[int]] = defaultdict(list)
        Solution.fuel = 0

        for road in roads:
            adjacency_list[road[0]].append(road[1])
            adjacency_list[road[1]].append(road[0])

        def dfs(node: int):
            people: int = 1
            visited.add(node)

            for neighbour in adjacency_list[node]:
                if neighbour in visited:
                    continue
                people += dfs(neighbour)

            if node == 0:
                return 0

            Solution.fuel += math.ceil(people / seats)
            return people

        visited: set[int] = set()
        dfs(0)

        return Solution.fuel


if __name__ == "__main__":
    assert Solution.minimum_fuel_cost(roads=[[0, 1], [0, 2], [0, 3]], seats=5) == 3
    assert (
        Solution.minimum_fuel_cost(
            roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2
        )
        == 7
    )
    assert Solution.minimum_fuel_cost(roads=[], seats=1) == 0
