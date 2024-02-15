class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sum_even_grandparent(root: TreeNode) -> int:
        def inner(
            node: TreeNode | None,
            parent_val: int | None,
            grand_parent_val: int | None,
        ):
            nonlocal result

            if node is None:
                return None

            if grand_parent_val is not None and grand_parent_val % 2 == 0:
                result += node.val

            inner(node.left, node.val, parent_val)
            inner(node.right, node.val, parent_val)

        result: int = 0
        inner(root, None, None)

        return result
