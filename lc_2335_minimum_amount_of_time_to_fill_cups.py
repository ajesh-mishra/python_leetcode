class Solution:
    def fill_cups(self, amount: list[int]) -> int:
        amount.sort()
        x, y, z = amount
        amount_sum = sum(amount)

        if x + y > z:
            return amount_sum // 2 + amount_sum % 2
        else:
            return z


if __name__ == "__main__":
    assert Solution().fill_cups(amount=[1, 4, 2]) == 4
    assert Solution().fill_cups(amount=[5, 4, 4]) == 7
    assert Solution().fill_cups(amount=[5, 0, 0]) == 5
