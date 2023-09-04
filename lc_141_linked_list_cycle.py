class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def has_cycle_1(head):
        list_node = set()
        while head is not None:
            if head in list_node:
                return True
            list_node.add(head)
            head = head.next
        return False

    @staticmethod
    def has_cycle(head: ListNode | None) -> bool:
        """Doesn't work! Don't know why?"""
        list_node = set()

        def dp(node: ListNode | None) -> bool:
            if node is None:
                return False
            if node in list_node:
                return True
            list_node.add(node)
            dp(node.next)

        return dp(head)


if __name__ == "__main__":
    assert Solution().has_cycle(None)
