class Solution:
    @staticmethod
    def eventual_safe_nodes(graph: list[list[int]]) -> list[int]:
        def dfs(node: int) -> bool:
            if node in safe:
                return True
            if node in visited:
                return False

            visited.add(node)

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            safe.add(node)
            return True

        visited: set[int] = set()
        safe: set[int] = {
            node for node, neighbour in enumerate(graph) if len(neighbour) == 0
        }

        for n in range(len(graph)):
            if n in visited:
                continue

            dfs(n)

        return sorted(list(safe), reverse=False)


if __name__ == "__main__":
    assert Solution.eventual_safe_nodes(
        graph=[[1, 2], [2, 3], [5], [0], [5], [], []]
    ) == [2, 4, 5, 6]
