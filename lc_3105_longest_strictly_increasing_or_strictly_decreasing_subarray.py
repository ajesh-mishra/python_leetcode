class Solution:
    @staticmethod
    def longestMonotonicSubarray(nums: list[int]) -> int:
        prev, trend, count, result = nums.pop(0), 0, 0, 0

        for num in nums:
            if num > prev:  # Increasing
                if trend == 1:
                    count += 1
                else:
                    trend = 1
                    count = 1
            elif num < prev:  # Decreasing
                if trend == -1:
                    count += 1
                else:
                    trend = -1
                    count = 1
            else:  # Equal
                trend = 0
                count = 0

            result = max(result, count)
            prev = num

        return result + 1


if __name__ == "__main__":
    assert Solution.longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]) == 2
    assert Solution.longestMonotonicSubarray(nums=[3, 3, 3, 3]) == 1
    assert Solution.longestMonotonicSubarray(nums=[3, 2, 1]) == 3
