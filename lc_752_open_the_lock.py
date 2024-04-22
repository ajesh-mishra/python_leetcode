from collections import deque
from typing import Deque


class Solution:
    @staticmethod
    def open_lock(deadends: list[str], target: str) -> int:
        queue: Deque[tuple[str, int]] = deque()
        queue.append(("0000", 0))
        visited: set[str] = set(deadends)

        while queue:
            node, depth = queue.popleft()

            if node == target:
                return depth

            for i in range(4):
                for delta in (-1, 1):
                    next_node = (
                        node[:i] + str((int(node[i]) + delta) % 10) + node[i + 1 :]
                    )
                    if next_node in visited:
                        continue
                    visited.add(next_node)
                    queue.append((next_node, depth + 1))

        return -1


if __name__ == "__main__":
    assert (
        Solution.open_lock(
            deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"
        )
        == 6
    )
    assert Solution.open_lock(deadends=["8888"], target="0009") == 1
    assert (
        Solution.open_lock(
            deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
            target="8888",
        )
        == -1
    )
