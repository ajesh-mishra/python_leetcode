class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        result, running_total = 0, 0

        for num in nums:
            running_total += num
            if running_total == 0:
                result += 1

        return result


if __name__ == "__main__":
    assert Solution().returnToBoundaryCount(nums=[2, 3, -5]) == 1
    assert Solution().returnToBoundaryCount(nums=[3, 2, -3, -4]) == 0
