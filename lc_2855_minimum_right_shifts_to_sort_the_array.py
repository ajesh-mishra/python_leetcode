class Solution:
    @staticmethod
    def minimum_right_shifts(nums: list[int]) -> int:
        prev: int | None = None
        first: int | None = None
        shift_point: int | None = None

        for index, num in enumerate(nums):
            if prev is None:
                prev = num
                first = num
                continue
            if num > prev and shift_point is None:
                prev = num
                continue
            if num < first and shift_point is None:
                shift_point = index
                prev = num
                continue
            if shift_point is not None and prev < num < first:
                prev = num
                continue
            return -1

        if shift_point is None:
            return 0

        return len(nums) - shift_point


if __name__ == "__main__":
    assert Solution().minimum_right_shifts([3, 4, 5, 1, 2]) == 2
    assert Solution().minimum_right_shifts([1, 3, 5]) == 0
    assert Solution().minimum_right_shifts([2, 1, 4]) == -1
