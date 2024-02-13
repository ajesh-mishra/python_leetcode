class Solution:
    @classmethod
    def create_adjacency_list(cls, n: int, edges: list[list[int]]) -> list[list[int]]:
        adjacency_list: list[list[int]] = [[] for _ in range(n)]

        for s, d in edges:
            adjacency_list[s].append(d)
            adjacency_list[d].append(s)

        return adjacency_list

    @classmethod
    def is_complete(
        cls, components: list[int], adjacency_list: list[list[int]]
    ) -> bool:
        is_complete = True

        for c in components:
            if len(adjacency_list[c]) + 1 != len(components):
                is_complete = False
                break

        return is_complete

    @staticmethod
    def count_complete_components(n: int, edges: list[list[int]]) -> int:
        adjacency_list: list[list[int]] = Solution.create_adjacency_list(n, edges)

        def dfs(node: int) -> None:
            if node in visited:
                return None

            visited.add(node)
            components.append(node)

            for neighbour in adjacency_list[node]:
                dfs(neighbour)

        visited: set[int] = set()
        components: list[int] = []
        count = 0

        for i in range(n):
            if i in visited:
                continue

            dfs(i)

            if Solution.is_complete(components, adjacency_list):
                count += 1

            components.clear()

        return count


if __name__ == "__main__":
    assert (
        Solution().count_complete_components(
            n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]
        )
        == 3
    )
    assert (
        Solution().count_complete_components(
            n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
        )
        == 1
    )
