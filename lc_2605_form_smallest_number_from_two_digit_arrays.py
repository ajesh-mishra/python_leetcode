class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        try:
            min_common_digit = min(set(nums1).intersection(set(nums2)))
        except ValueError:
            pass
        else:
            return min_common_digit

        digit_1 = min(nums1)
        digit_2 = min(nums2)

        if digit_1 < digit_2:
            return digit_1 * 10 + digit_2
        else:
            return digit_2 * 10 + digit_1


if __name__ == "__main__":
    assert Solution().minNumber(nums1=[4, 1, 3], nums2=[5, 7]) == 15
    assert Solution().minNumber(nums1=[3, 5, 2, 6], nums2=[3, 1, 7]) == 3
