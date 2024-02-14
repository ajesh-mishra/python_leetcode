from typing import Generator, Any


class Solution:
    @staticmethod
    def rearrange_array(nums: list[int]) -> list[int]:
        positives: Generator[int, None, Any] = (num for num in nums if num >= 0)
        negatives: Generator[int, None, Any] = (num for num in nums if num < 0)

        result: list[int] = []

        while True:
            try:
                result.extend([next(positives), next(negatives)])
            except StopIteration:
                break

        return result


if __name__ == "__main__":
    assert Solution.rearrange_array(nums=[3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
    assert Solution.rearrange_array(nums=[-1, 1]) == [1, -1]
