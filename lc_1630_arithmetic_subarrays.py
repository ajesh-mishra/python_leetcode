class Solution:
    @staticmethod
    def check_arithmetic_subarrays(
        nums: list[int], l: list[int], r: list[int]
    ) -> list[bool]:
        result: list[bool] = []
        for start, end in zip(l, r):
            subarray = nums[start : end + 1]
            subarray.sort()
            s = {subarray[i + 1] - subarray[i] for i in range(len(subarray) - 2 + 1)}
            if len(s) == 1:
                result.append(True)
            else:
                result.append(False)

        return result


if __name__ == "__main__":
    # print(
    #     Solution().check_arithmetic_subarrays(
    #         nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]
    #     )
    # )
    # print(
    #     Solution().check_arithmetic_subarrays(
    #         nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
    #         l=[0, 1, 6, 4, 8, 7],
    #         r=[4, 4, 9, 7, 9, 10],
    #     )
    # )
    assert Solution().check_arithmetic_subarrays(
        nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]
    ) == [True, False, True]
    assert Solution().check_arithmetic_subarrays(
        nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
        l=[0, 1, 6, 4, 8, 7],
        r=[4, 4, 9, 7, 9, 10],
    ) == [False, True, False, False, True, True]
    # assert Solution().checkArithmeticSubarrays() ==
