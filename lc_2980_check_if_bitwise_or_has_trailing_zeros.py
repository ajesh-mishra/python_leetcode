class Solution:
    @staticmethod
    def has_trailing_zeros(nums: list[int]) -> bool:
        return len(list(filter(lambda num: f"{num:b}".endswith("0"), [num for num in nums]))) >= 2


if __name__ == "__main__":
    assert Solution().has_trailing_zeros(nums=[1, 2, 3, 4, 5])
    assert Solution().has_trailing_zeros(nums=[2, 4, 8, 16])
    assert not Solution().has_trailing_zeros(nums=[1, 3, 5, 7, 9])
