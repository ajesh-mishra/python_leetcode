class Solution:
    @staticmethod
    def maximum_strong_pair_xor(nums: list[int]) -> int:
        strongest_xor, length = 0, len(nums)

        for i in range(length):
            for j in range(length):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    strongest_xor = max(strongest_xor, nums[i] ^ nums[j])

        return strongest_xor


if __name__ == "__main__":
    assert Solution().maximum_strong_pair_xor(nums=[1, 2, 3, 4, 5]) == 7
    assert Solution().maximum_strong_pair_xor(nums=[5, 6, 25, 30]) == 7
    assert Solution().maximum_strong_pair_xor(nums=[10, 100]) == 0
    assert Solution().maximum_strong_pair_xor(nums=[1, 2, 2, 1, 2]) == 3
