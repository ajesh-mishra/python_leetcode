class Solution:
    @staticmethod
    def find_max_k(nums: list[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == 0:
                return nums[j]
            if nums[j] <= 0 or nums[i] >= 0:
                break
            if abs(nums[i]) < nums[j]:
                j -= 1
            if abs(nums[i]) > nums[j]:
                i += 1

        return -1


if __name__ == "__main__":
    assert Solution.find_max_k(nums=[-1, 2, -3, 3]) == 3
    assert Solution.find_max_k(nums=[-1, 10, 6, 7, -7, 1]) == 7
    assert Solution.find_max_k(nums=[-10, 8, 6, 7, -2, -3]) == -1
