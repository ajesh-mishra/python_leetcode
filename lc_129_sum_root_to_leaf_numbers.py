class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sum_numbers(root: TreeNode | None) -> int:
        value: int = 0

        def dfs(node: TreeNode | None, path: int) -> None:
            nonlocal value

            path = (path * 10) + node.val

            if node.left is None and node.right is None:
                value += path
                return None

            if node.left is not None:
                dfs(node.left, path)

            if node.right is not None:
                dfs(node.right, path)

        dfs(root, 0)
        return value
