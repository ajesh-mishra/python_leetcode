class Solution:
    def missing_integer(self, nums: list[int]) -> int:
        sequential_prefix = 0

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                sequential_prefix = i
                break

        sum_sequential_prefix = (
            sum(nums) if sequential_prefix == 0 else sum(nums[:sequential_prefix])
        )

        for i in range(sum_sequential_prefix, sum_sequential_prefix + len(nums)):
            if i not in nums:
                return i

        return max(nums) + 1


if __name__ == "__main__":
    assert Solution().missing_integer(nums=[1, 2, 3, 2, 5]) == 6
    assert Solution().missing_integer(nums=[3, 4, 5, 1, 12, 14, 13]) == 15
    assert Solution().missing_integer(nums=[29, 30, 31, 32, 33, 34, 35, 36, 37]) == 297
