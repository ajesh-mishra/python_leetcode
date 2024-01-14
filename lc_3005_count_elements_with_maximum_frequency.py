class Solution:
    def max_frequency_elements(self, nums: list[int]) -> int:
        map_nums = {}

        for num in nums:
            if num in map_nums:
                map_nums[num] += 1
            else:
                map_nums[num] = 1

        max_frequency = max(map_nums.values())
        max_frequency_count = list(map_nums.values()).count(max_frequency)

        return max_frequency * max_frequency_count


if __name__ == "__main__":
    assert Solution().max_frequency_elements(nums=[1, 2, 2, 3, 1, 4]) == 4
    assert Solution().max_frequency_elements(nums=[1, 2, 3, 4, 5]) == 5
