class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def smallest_from_leaf(root: TreeNode | None) -> str:
        paths: list[str] = []

        def dfs(node: TreeNode | None, path: str):
            nonlocal paths

            path += chr(node.val + 97)

            if node.left is None and node.right is None:
                paths.append(path)

            if node.left is not None:
                dfs(node.left, path)

            if node.right is not None:
                dfs(node.right, path)

        dfs(root, "")
        return sorted(paths)[0]
