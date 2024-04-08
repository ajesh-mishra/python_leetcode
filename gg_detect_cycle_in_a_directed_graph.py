class Solution:
    @staticmethod
    def is_cyclic(v, adj):
        def dfs(node) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for neighbour in adj[node]:
                if not adj[neighbour]:
                    continue
                if path_visited[neighbour]:
                    return True

                path_visited[neighbour] = True

                if dfs(neighbour):
                    return True

                path_visited[neighbour] = False

            return False

        visited = set()
        path_visited = [False for _ in range(len(adj))]

        for i, a in enumerate(adj):
            if i in visited or not a:
                continue

            path_visited[i] = True

            if dfs(i):
                return 1

            path_visited[i] = False

        return 0


if __name__ == "__main__":
    assert Solution.is_cyclic(4, [[1], [2], [3], [0]]) == 1
