class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def find_bottom_left_value(root: TreeNode | None) -> int:
        queue: list[tuple[TreeNode | None, int]] = [(root, 0)]
        left_most: tuple[int, int] = (root.val, 0)

        while len(queue) != 0:
            node, distance = queue.pop(0)

            if left_most[1] < distance:
                left_most = (node.val, distance)

            if node.left is not None:
                queue.append((node.left, distance + 1))

            if node.right is not None:
                queue.append((node.right, distance + 1))

        return left_most[0]


if __name__ == "__main__":
    tn = TreeNode()
    print(Solution.find_bottom_left_value(tn))
