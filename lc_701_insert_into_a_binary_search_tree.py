class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def insert_into_bst(root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val=val)

        def inner(r: TreeNode | None) -> None:
            if val < r.val:
                if r.left is not None:
                    inner(r.left)
                else:
                    r.left = TreeNode(val=val)
            else:
                if r.right is not None:
                    inner(r.right)
                else:
                    r.right = TreeNode(val=val)

        inner(root)
        return root
