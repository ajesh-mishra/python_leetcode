class Solution:
    @staticmethod
    def largest_sum_after_k_negations(nums: list[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)):
            if k <= 0:
                break
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1

        total = sum(nums)

        if k % 2 != 0:
            total -= min(nums) * 2

        return total


if __name__ == "__main__":
    assert Solution().largest_sum_after_k_negations(nums=[4, 2, 3], k=1) == 5
    assert Solution().largest_sum_after_k_negations(nums=[3, -1, 0, 2], k=3) == 6
    assert Solution().largest_sum_after_k_negations(nums=[2, -3, -1, 5, -4], k=2) == 13
