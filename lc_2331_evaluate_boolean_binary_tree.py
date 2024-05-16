class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def evaluate_tree(root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None):
            if node.val == 1 or node.val == 0:
                return node.val

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == 2:
                return left | right
            else:
                return left & right

        return dfs(root) == 1
