class Solution:
    @staticmethod
    def max_product(nums: list[int]) -> int:
        nums_minus_one: list[int] = list(map(lambda x: x - 1, nums))
        nums_minus_one.sort(reverse=True)
        return nums_minus_one[0] * nums_minus_one[1]


if __name__ == "__main__":
    assert Solution().max_product(nums=[3, 4, 5, 2]) == 12
    assert Solution().max_product(nums=[1, 5, 4, 5]) == 16
    assert Solution().max_product(nums=[3, 7]) == 12
