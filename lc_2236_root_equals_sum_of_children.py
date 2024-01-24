class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        return root.val == root.left.val + root.right.val


if __name__ == "__main__":
    assert Solution().checkTree()
