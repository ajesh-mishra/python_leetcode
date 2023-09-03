from itertools import combinations


class Solution:
    @staticmethod
    def count_pairs(nums: list[int], target: int) -> int:
        return len([pair for pair in combinations(nums, 2) if sum(pair) < target])


if __name__ == "__main__":
    assert Solution().count_pairs(nums=[-1, 1, 2, 3, 1], target=2) == 3
    assert Solution().count_pairs(nums=[-6, 2, 5, -2, -7, -1, 3], target=-2) == 10
