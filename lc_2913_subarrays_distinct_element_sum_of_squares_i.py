class Solution:
    @staticmethod
    def sum_counts(nums: list[int]) -> int:
        length, result = len(nums), 0

        for start in range(0, length):
            for window in range(1, length + 1):
                if start + window > length:
                    continue
                result += pow(len(set(nums[start : start + window])), 2)

        return result


if __name__ == "__main__":
    # print(Solution().sumCounts(nums=[1, 2, 1]))
    assert Solution().sum_counts(nums=[1, 2, 1]) == 15
    assert Solution().sum_counts(nums=[1, 1]) == 3
