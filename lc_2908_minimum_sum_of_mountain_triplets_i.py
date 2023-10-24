import sys


class Solution:
    @staticmethod
    def minimum_sum(nums: list[int]) -> int:
        length = len(nums)
        min_sum = sys.maxsize

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] < nums[j] > nums[k]:
                        min_sum = min(min_sum, nums[i] + nums[j] + nums[k])

        if min_sum == sys.maxsize:
            return -1

        return min_sum


if __name__ == "__main__":
    # print(Solution().minimumSum(nums=[8, 6, 1, 5, 3]))
    assert Solution().minimum_sum(nums=[8, 6, 1, 5, 3]) == 9
    assert Solution().minimum_sum(nums=[5, 4, 8, 7, 10, 2]) == 13
    assert Solution().minimum_sum(nums=[6, 5, 4, 3, 4, 5]) == -1
