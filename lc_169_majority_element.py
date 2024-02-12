from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int | None:
        half_length = len(nums) // 2
        map: dict[int, int] = defaultdict(int)

        for num in nums:
            map[num] += 1
            if map[num] > half_length:
                return num