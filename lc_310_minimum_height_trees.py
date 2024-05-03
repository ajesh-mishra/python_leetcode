from collections import defaultdict, deque
from typing import Deque


class Solution:
    @staticmethod
    def find_min_height_trees(n: int, edges: list[list[int]]) -> list[int]:
        if not edges:
            return [x for x in range(n)]

        adjancy_list: defaultdict[int, list[int]] = defaultdict(list)

        for edge in edges:
            adjancy_list[edge[0]].append(edge[1])
            adjancy_list[edge[1]].append(edge[0])

        possible_roots = [k for k in adjancy_list.keys()]

        def bfs(r: int) -> int:
            max_depth: int = 0
            visited: set[int] = set()

            queue: Deque[tuple[int, int]] = deque()
            queue.append((r, 0))

            while queue:
                node, d = queue.popleft()
                visited.add(node)
                max_depth = max(max_depth, d)

                for neighbour in adjancy_list[node]:
                    if neighbour in visited:
                        continue
                    queue.append((neighbour, d + 1))

            return max_depth

        depth_map: defaultdict[int, int] = defaultdict(int)

        for root in possible_roots:
            depth_map[root] = bfs(root)

        min_depth = min(depth_map.values())

        print(f"{depth_map=}")
        return [key for key, value in depth_map.items() if value == min_depth]


if __name__ == "__main__":
    # print(Solution.find_min_height_trees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
    assert Solution.find_min_height_trees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1]
    assert Solution.find_min_height_trees(
        n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    ) == [3, 4]
