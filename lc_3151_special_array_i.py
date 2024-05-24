class Solution:
    @staticmethod
    def is_array_special(nums: list[int]) -> bool:
        prev: int | None = None

        for num in nums:
            curr = 1 if num & 1 else 0

            if prev is not None and not prev ^ curr:
                return False

            prev = curr

        return True


if __name__ == "__main__":
    assert Solution.is_array_special(nums=[1])
    assert Solution.is_array_special(nums=[2, 1, 4])
    assert not Solution.is_array_special(nums=[4, 3, 1, 6])
