class Solution:
    @staticmethod
    def minimum_average(nums: list[int]) -> float:
        average: float | None = None
        nums.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            if average is None:
                average = (nums[i] + nums[j]) / 2
            else:
                average = min(average, (nums[i] + nums[j]) / 2)
            i += 1
            j -= 1

        return average


if __name__ == "__main__":
    assert Solution.minimum_average([7, 8, 3, 4, 15, 13, 4, 1]) == 5.5
    assert Solution.minimum_average([7, 8, 3, 4, 15, 13, 4, 1]) == 5.5
    assert Solution.minimum_average([1, 2, 3, 7, 8, 9]) == 5.0
