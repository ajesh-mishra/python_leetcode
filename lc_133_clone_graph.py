class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    @staticmethod
    def clone_graph(node: Node | None) -> Node | None:
        visited: dict[int, node] = {}

        def dfs(n: Node | None) -> Node | None:
            if n.val in visited:
                return None

            new_node = Node(n.val)
            visited[n.val] = new_node

            for neighbor in n.neighbors:
                if neighbor.val not in visited:
                    new_node.neighbors.append(dfs(neighbor))
                else:
                    new_node.neighbors.append(visited[neighbor.val])

            return new_node

        return dfs(node)
