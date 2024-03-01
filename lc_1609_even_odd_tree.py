class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import DefaultDict


class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        queue: list[tuple[int, int]] = [(root, 0)]
        distances: DefaultDict[int, list[int]] = defaultdict(list)

        while len(queue) != 0:
            node, distance = queue.pop(0)

            if node is None:
                continue

            distances[distance].append(node.val)
            queue.append((node.left, distance + 1))
            queue.append((node.right, distance + 1))

        for key, values in distances.items():
            if (
                key % 2 == 0
                and all(map(lambda x: x % 2 != 0, values))
                and all(
                    map(lambda x: values[x] < values[x + 1], range(len(values) - 1))
                )
            ):
                continue

            if (
                key % 2 != 0
                and all(map(lambda x: x % 2 == 0, values))
                and all(
                    map(lambda x: values[x] > values[x + 1], range(len(values) - 1))
                )
            ):
                continue

            return False

        return True
