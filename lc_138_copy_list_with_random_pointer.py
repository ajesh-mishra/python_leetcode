class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    @staticmethod
    def copy_random_list(head: Node | None) -> Node | None:
        if head is None:
            return None

        old_list, new_list = [], []

        while head is not None:
            new_node = Node(head.val)
            new_node.random = head.random

            if len(new_list) != 0:
                new_list[-1].next = new_node

            new_list.append(new_node)
            old_list.append(head)
            head = head.next

        for node_1 in new_list:
            if node_1.random is None:
                continue
            for index, node_2 in enumerate(old_list):
                if node_1.random == node_2:
                    node_1.random = new_list[index]

        return new_list[0]


if __name__ == "__main__":
    Solution().copy_random_list(None)
