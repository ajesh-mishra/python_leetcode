class Solution:
    @staticmethod
    def valid_path_bfs(
        n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        adjacency_list: list[list[int]] = [[] for _ in range(n)]

        for edge in edges:
            x, y = edge[0], edge[1]
            adjacency_list[x].append(y)
            adjacency_list[y].append(x)

        queue: list[int] = [source]
        visited: set[int] = set()

        def bfs(root: int) -> bool:
            if root == destination:  # Base Case
                return True

            visited.add(root)  # Manipulating the Queue & Visited List
            queue.extend(
                [value for value in adjacency_list[root] if value not in visited]
            )

            while len(queue) != 0:  # Recursive Relationship
                if bfs(queue.pop(0)):
                    return True

            return False  # False Case

        return bfs(source)

    @staticmethod
    def valid_path_dfs(
        n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        adjacency_list: list[list[int]] = [[] for _ in range(n)]

        for edge in edges:
            x, y = edge[0], edge[1]
            adjacency_list[x].append(y)
            adjacency_list[y].append(x)

        visited: set[int] = set()

        def dfs(root: int) -> bool | list[int]:
            if root == destination:  # Base Case
                return True

            visited.add(root)  # Updating Visited List

            for neighbour in adjacency_list[root]:  # Recursive Relationship
                if neighbour in visited:
                    continue
                if dfs(neighbour):
                    return True

            return False  # False Case

        return dfs(source)


if __name__ == "__main__":
    assert Solution().valid_path_bfs(
        n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2
    )
    assert Solution().valid_path_bfs(
        n=10,
        edges=[
            [0, 7],
            [0, 8],
            [6, 1],
            [2, 0],
            [0, 4],
            [5, 8],
            [4, 7],
            [1, 3],
            [3, 5],
            [6, 5],
        ],
        source=7,
        destination=5,
    )
    assert Solution().valid_path_bfs(
        n=10,
        edges=[
            [4, 3],
            [1, 4],
            [4, 8],
            [1, 7],
            [6, 4],
            [4, 2],
            [7, 4],
            [4, 0],
            [0, 9],
            [5, 4],
        ],
        source=5,
        destination=9,
    )
    assert not Solution().valid_path_bfs(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
