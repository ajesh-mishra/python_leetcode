class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Deque


class Solution:
    def is_symmetric(self, root: TreeNode | None) -> bool:
        def bfs(r: TreeNode | None, is_left: bool) -> list[int | None]:
            queue: Deque[TreeNode | None] = deque()
            queue.append(r)
            value: list[int | None] = []

            while queue:
                node: TreeNode | None = queue.popleft()

                if node is None:
                    value.append(None)
                    continue

                value.append(node.val)

                if is_left:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.append(node.right)
                    queue.append(node.left)

            print(f"{value=}")
            return value

        return bfs(root.left, True) == bfs(root.right, False)
