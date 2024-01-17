import math


class Solution:
    def pick_gifts(self, gifts: list[int], k: int) -> int:
        for _ in range(k):
            pos = gifts.index(max(gifts))
            gifts[pos] = math.isqrt(gifts[pos])

        return sum(gifts)


if __name__ == "__main__":
    assert Solution().pick_gifts(gifts=[25, 64, 9, 4, 100], k=4) == 29
    assert Solution().pick_gifts(gifts=[1, 1, 1, 1], k=4) == 4
