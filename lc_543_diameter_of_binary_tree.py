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

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return diameter
