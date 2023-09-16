class Solution:
    def alternating_subarray(self, nums: list[int]) -> int:
        alternate_array: list[int] = []
        prev, count, result = 0, 0, 0

        for i in range(len(nums) - 1):
            alternate_array.append(nums[i + 1] - nums[i])

        for s in alternate_array:
            if (s == 1 and (prev == -1 or count == 0)) or (s == -1 and prev == 1):
                count += 1
                prev = s
                continue
            prev = s
            result = max(result, count)
            if s == 1 and prev != -1:
                count = 1
            else:
                count = 0

        if count != 0:
            result = max(result, count)
        if result == 0:
            return -1
        return result + 1


if __name__ == "__main__":
    assert Solution().alternating_subarray([2, 3, 4, 3, 4]) == 4
    assert Solution().alternating_subarray([4, 5, 6]) == 2
