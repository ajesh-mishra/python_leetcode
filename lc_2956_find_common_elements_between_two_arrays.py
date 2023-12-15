class Solution:
    @staticmethod
    def find_intersection_values(nums1: list[int], nums2: list[int]) -> list[int]:
        common = set(nums1).intersection(set(nums2))
        return [
            len([num for num in nums1 if num in common]),
            len([num for num in nums2 if num in common]),
        ]


if __name__ == "__main__":
    assert Solution().find_intersection_values(
        nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]
    ) == [3, 4]
    assert Solution().find_intersection_values(nums1=[3, 4, 2, 3], nums2=[1, 5]) == [
        0,
        0,
    ]
