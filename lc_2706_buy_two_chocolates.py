class Solution:
    def buy_choco(self, prices: list[int], money: int) -> int:
        prices.sort()
        if (left_over := money - sum(prices[0:2])) >= 0:
            return left_over
        else:
            return money


if __name__ == "__main__":
    assert Solution().buy_choco(prices=[1, 2, 2], money=3) == 0
    assert Solution().buy_choco(prices=[3, 2, 3], money=3) == 3
