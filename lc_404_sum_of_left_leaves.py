from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
        def inner(root: Optional[TreeNode], is_left: bool) -> int:
            if root is None:
                return 0

            _sum = 0
            if root.left is None and root.right is None and is_left:
                _sum = root.val

            return (
                _sum + inner(root.left, is_left=True) + inner(root.right, is_left=False)
            )

        return inner(root=root, is_left=False)


if __name__ == "__main__":
    print(Solution().sum_of_left_leaves(root=TreeNode()))
