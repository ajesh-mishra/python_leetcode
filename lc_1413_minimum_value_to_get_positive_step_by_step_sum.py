class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        minimum_value, prev = 0, 0
        for num in nums:
            prev += num
            minimum_value = min(minimum_value, prev)
        return abs(minimum_value - 1)


if __name__ == "__main__":
    assert Solution().minStartValue(nums=[-3, 2, -3, 4, 2]) == 5
    assert Solution().minStartValue(nums=[1, -2, -3]) == 5
    assert Solution().minStartValue(nums=[1, 2]) == 1
