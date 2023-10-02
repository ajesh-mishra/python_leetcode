class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        length, result = len(nums), 0
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    result = max(result, (nums[i] - nums[j]) * nums[k])
        return result


if __name__ == "__main__":
    assert Solution().maximumTripletValue(nums=[12, 6, 1, 2, 7]) == 77
    assert Solution().maximumTripletValue(nums=[1, 10, 3, 4, 19]) == 133
    assert Solution().maximumTripletValue(nums=[1, 2, 3]) == 0
