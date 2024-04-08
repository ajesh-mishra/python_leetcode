class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        def inner(n: LinkedList | None, result: list[int]) -> list[int | None]:
            if n is None:
                return result

            result.append(n.val)
            return inner(n.next, result)

        return str(inner(self, []))


def create_linked_list(nums: list[int]) -> LinkedList:
    # def inner(n: list[int]) -> LinkedList | None:
    #     if len(n) == 0:
    #         return None
    #
    #     new_num = n.pop(0)
    #     prev_ll = inner(n)
    #     new_ll = LinkedList(new_num, prev_ll)
    #     return new_ll
    #
    # return inner(nums)

    def inner(n: list[int], ll: LinkedList | None) -> LinkedList:
        if len(n) == 0:
            return ll

        new_num = n.pop()
        new_ll = LinkedList(new_num, ll)
        return inner(n, new_ll)

    return inner(nums, None)


def merge_linked_list(ll1: LinkedList | None, ll2: LinkedList | None) -> LinkedList | None:
    def inner(a: LinkedList | None, b: LinkedList | None) -> LinkedList | None:
        if a is None:
            return b

        if b is None:
            return a

        if a.val <= b.val:
            a.next = inner(a.next, b)
            return a

        if a.val > b.val:
            b.next = inner(a, b.next)
            return b

    return inner(ll1, ll2)



if __name__ == "__main__":
    ll1 = create_linked_list([1, 3, 5, 7])
    print(ll1)
    ll2 = create_linked_list([2, 3, 4, 6, 8])
    print(ll2)
    ll = merge_linked_list(ll1, ll2)
    print(ll)
