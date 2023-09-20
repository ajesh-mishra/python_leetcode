class Solution:
    @staticmethod
    def sum_indices_with_k_set_bits_1(nums: list[int], k: int) -> int:
        result: int = 0
        for index, num in enumerate(nums):
            if len([1 for c in f"{index:b}" if c == "1"]) == k:
                result += num
        return result

    @staticmethod
    def sum_indices_with_k_set_bits(nums: list[int], k: int) -> int:
        return sum(
            [
                num
                for index, num in enumerate(nums)
                if len([1 for c in f"{index:b}" if c == "1"]) == k
            ]
        )


if __name__ == "__main__":
    assert Solution().sum_indices_with_k_set_bits(nums=[5, 10, 1, 5, 2], k=1) == 13
    assert Solution().sum_indices_with_k_set_bits(nums=[4, 3, 2, 1], k=2) == 1
