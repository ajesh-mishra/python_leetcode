from collections import deque
from typing import Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def add_one_row(root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        if depth == 1:
            return TreeNode(val=val, left=root)

        queue: Deque[tuple[TreeNode, int]] = deque()
        queue.append((root, 1))

        while queue:
            node, curr_depth = queue.popleft()
            original_left, original_right = node.left, node.right

            if curr_depth + 1 == depth:
                node.left = TreeNode(val=val, left=original_left)
                node.right = TreeNode(val=val, right=original_right)

            if original_left is not None:
                queue.append((original_left, curr_depth + 1))
            if original_right is not None:
                queue.append((original_right, curr_depth + 1))

        return root
