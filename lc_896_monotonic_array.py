class Solution:
    def is_monotonic(self, nums: list[int]) -> bool:
        is_increasing, is_decreasing = True, True

        for i in range(1, len(nums)):
            if nums[i - 1] - nums[i] > 0:
                is_increasing = False
            elif nums[i - 1] - nums[i] < 0:
                is_decreasing = False
            if not is_increasing and not is_decreasing:
                return False

        return is_increasing or is_decreasing


if __name__ == "__main__":
    assert Solution().is_monotonic([1, 2, 2, 3])
    assert Solution().is_monotonic([6, 5, 4, 4])
    assert not Solution().is_monotonic([1, 3, 2])
