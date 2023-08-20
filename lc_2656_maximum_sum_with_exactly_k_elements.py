class Solution:
    @staticmethod
    def maximize_sum(nums: list[int], k: int) -> int:
        return (max(nums) * k) + sum(range(k))


if __name__ == '__main__':
    print(Solution().maximize_sum(nums=[1, 2, 3, 4, 5], k=3))
    print(Solution().maximize_sum(nums=[5, 5, 5], k=2))

    assert Solution().maximize_sum(nums=[1, 2, 3, 4, 5], k=3) == 18
    assert Solution().maximize_sum(nums=[5, 5, 5], k=2) == 11
