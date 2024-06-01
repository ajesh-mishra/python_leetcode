class Solution:
    @staticmethod
    def special_array(nums: list[int]) -> int:
        prev, length = 0, len(nums)
        nums.sort()

        for index, num in enumerate(nums):
            if (remaining := length - index) <= num and prev < remaining:
                return remaining
            prev = num

        return -1


if __name__ == "__main__":
    assert Solution.special_array(nums=[3, 5]) == 2
    assert Solution.special_array(nums=[0, 0]) == -1
    assert Solution.special_array(nums=[0, 4, 3, 0, 4]) == 3
    assert Solution.special_array(nums=[3, 6, 7, 7, 0]) == -1
