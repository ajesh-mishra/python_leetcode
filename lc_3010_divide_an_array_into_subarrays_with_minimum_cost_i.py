class Solution:
    @staticmethod
    def minimum_cost(nums: list[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])


if __name__ == "__main__":
    assert Solution().minimum_cost(nums=[1, 2, 3, 12]) == 6
    assert Solution().minimum_cost(nums=[5, 4, 3]) == 12
    assert Solution().minimum_cost(nums=[10, 3, 1, 1]) == 12
