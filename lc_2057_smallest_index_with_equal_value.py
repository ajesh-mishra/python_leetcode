class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for index, num in enumerate(nums):
            if index % 10 == num:
                return index

        return -1