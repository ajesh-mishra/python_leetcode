class Solution:
    @staticmethod
    def find_duplicate(nums: list[int]) -> int:
        nums_set: set[int] = set()
        for num in nums:
            if num in nums_set:
                return num
            nums_set.add(num)


if __name__ == "__main__":
    assert Solution().find_duplicate([1, 3, 4, 2, 2]) == 2
    assert Solution().find_duplicate([3, 1, 3, 4, 2]) == 3
    assert Solution().find_duplicate([2, 2, 2, 2, 2]) == 2
