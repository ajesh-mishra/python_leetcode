class Solution:
    @staticmethod
    def number_of_points(nums: list[list[int]]) -> int:
        return len({n for num in nums for n in range(num[0], num[1] + 1)})


if __name__ == "__main__":
    assert Solution().number_of_points([[3, 6], [1, 5], [4, 7]]) == 7
    assert Solution().number_of_points([[1, 3], [5, 8]]) == 7
