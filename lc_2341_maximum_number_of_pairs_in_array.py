class Solution:
    @staticmethod
    def number_of_pairs(nums: list[int]) -> list[int]:
        mapped_nums: dict[int, int] = {}

        for num in nums:
            if num in mapped_nums:
                mapped_nums[num] += 1
            else:
                mapped_nums[num] = 1

        re_map: list[tuple[int, int]] = [
            (value // 2, value % 2) for value in mapped_nums.values()
        ]

        return [
            sum([value[0] for value in re_map]),
            sum([value[1] for value in re_map]),
        ]


if __name__ == "__main__":
    assert Solution().number_of_pairs(nums=[1, 3, 2, 1, 3, 2, 2]) == [3, 1]
    assert Solution().number_of_pairs(nums=[1, 1]) == [1, 0]
    assert Solution().number_of_pairs(nums=[0]) == [0, 1]
