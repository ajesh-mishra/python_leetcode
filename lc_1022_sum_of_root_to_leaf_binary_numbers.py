class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sum_root_to_leaf(root: TreeNode | None) -> int:
        nums: list[str] = []

        def dp(node, val: str = '') -> None:
            if node.left is None and node.right is None:
                nums.append(val + str(node.val))
                return
            if node.left is not None:
                dp(node.left, val + str(node.val))
            if node.right is not None:
                dp(node.right, val + str(node.val))

        dp(root)
        return sum([int(num, 2) for num in nums])


if __name__ == '__main__':
    print(Solution().sum_root_to_leaf())
