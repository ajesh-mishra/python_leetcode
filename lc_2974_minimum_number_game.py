class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums


if __name__ == "__main__":
    # print(Solution().numberGame(nums=[5, 4, 2, 3]))
    assert Solution().numberGame(nums=[5, 4, 2, 3]) == [3, 2, 5, 4]
    assert Solution().numberGame(nums=[2, 5]) == [5, 2]
