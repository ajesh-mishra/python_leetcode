class Solution:
    def find_indices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        length = len(nums)

        if length <= indexDifference:
            return [-1, -1]

        for i in range(0, length - indexDifference):
            for j in range(i + indexDifference, length):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1, -1]


if __name__ == "__main__":
    assert Solution().find_indices(
        nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4
    ) == [0, 3]
    assert Solution().find_indices(
        nums=[2, 1], indexDifference=0, valueDifference=0
    ) == [0, 0]
    assert Solution().find_indices(
        nums=[1, 2, 3], indexDifference=2, valueDifference=4
    ) == [-1, -1]
    assert Solution().find_indices(
        nums=[5, 10], indexDifference=1, valueDifference=2
    ) == [0, 1]
