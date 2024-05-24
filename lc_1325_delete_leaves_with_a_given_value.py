class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def remove_leaf_nodes(root: TreeNode | None, target: int) -> TreeNode | None:
        def dfs(node: TreeNode | None):
            if node.left is not None:
                if dfs(node.left):
                    node.left = None

            if node.right is not None:
                if dfs(node.right):
                    node.right = None

            if node.left is None and node.right is None and node.val == target:
                return True

        dfs(root)

        if root.left is None and root.right is None and root.val == target:
            return None

        return root
