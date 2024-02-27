class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        diameter: int = 0

        def dfs(node: TreeNode | None):
            nonlocal diameter

            if node.left is None and node.right is None:
                return 0

            left = right = 0

            if node.left is not None:
                left = 1 + dfs(node.left)

            if node.right is not None:
                right = 1 + dfs(node.right)

            diameter = max(diameter, left + right)
            return max(left, right)

        dfs(root)
        return diameter
