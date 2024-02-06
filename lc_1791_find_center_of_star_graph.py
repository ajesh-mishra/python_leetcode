class Solution:
    def find_center(self, edges: list[list[int]]) -> int:
        edge_set = set()
        prev_len = 0
        for node in [n for edge in edges for n in edge]:
            edge_set.add(node)
            new_len = len(edge_set)
            if prev_len == new_len:
                return node
            prev_len = new_len


if __name__ == "__main__":
    assert Solution().find_center(edges=[[1, 2], [2, 3], [4, 2]]) == 2
    assert Solution().find_center(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
