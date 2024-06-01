class Solution:
    @staticmethod
    def number_of_pairs(nums1: list[int], nums2: list[int], k: int) -> int:
        return len([True for i in nums1 for j in nums2 if i % (j * k) == 0])


if __name__ == "__main__":
    assert Solution.number_of_pairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1) == 5
    assert Solution.number_of_pairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3) == 2
    # assert Solution.numberOfPairs() ==
