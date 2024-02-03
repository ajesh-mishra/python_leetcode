class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverse_list(head: ListNode | None) -> ListNode | None:
        def inner(h: ListNode | None, result) -> ListNode | None:
            if h is None:
                return result

            curr = ListNode(h.val)
            curr.next = result

            return inner(h.next, curr)

        return inner(head, None)
