class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        value: int = 0
        while nums:
            first = nums.pop(0)
            try:
                current = int(str(first) + str(nums.pop()))
            except IndexError:
                current = first
            value += current

        return value


if __name__ == "__main__":
    assert Solution().findTheArrayConcVal(nums=[7, 52, 2, 4]) == 596
    assert Solution().findTheArrayConcVal(nums=[5, 14, 13, 8, 12]) == 673
