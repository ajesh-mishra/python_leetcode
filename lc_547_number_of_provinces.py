class Solution:
    @staticmethod
    def findCircleNum(isConnected: list[list[int]]) -> int:
        visited: list[int] = []
        provinces_count: int = 0

        def inner(n: int):
            if n in visited:
                return None

            visited.append(n)

            for neighbour in [
                index
                for index, node in enumerate(isConnected[n - 1], start=1)
                if node == 1
            ]:
                inner(neighbour)

        for node in [i for i in range(1, len(isConnected) + 1)]:
            if node not in visited:
                inner(node)
                provinces_count += 1

        return provinces_count
