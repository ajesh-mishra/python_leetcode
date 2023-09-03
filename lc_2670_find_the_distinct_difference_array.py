class Solution:
    @staticmethod
    def distinct_difference_array(nums: list[int]) -> list[int]:
        result: list[int] = []
        for index in range(len(nums)):
            diff = len(set(nums[0 : index + 1])) - len(set(nums[index + 1 :]))
            result.append(diff)

        return result


if __name__ == "__main__":
    assert Solution().distinct_difference_array(nums=[1, 2, 3, 4, 5]) == [
        -3,
        -1,
        1,
        3,
        5,
    ]
    assert Solution().distinct_difference_array(nums=[3, 2, 3, 4, 2]) == [
        -2,
        -1,
        0,
        2,
        3,
    ]
