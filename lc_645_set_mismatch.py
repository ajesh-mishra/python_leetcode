class Solution:
    @staticmethod
    def find_error_nums(nums: list[int]) -> list[int]:
        length, sum_nums, sum_nums_set = len(nums), sum(nums), sum(set(nums))
        return [sum_nums - sum_nums_set, (length * (length + 1) // 2) - sum_nums_set]


if __name__ == "__main__":
    assert Solution().find_error_nums(nums=[1, 2, 2, 4]) == [2, 3]
    assert Solution().find_error_nums(nums=[1, 1]) == [1, 2]
