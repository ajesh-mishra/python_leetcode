from itertools import chain


class Solution:
    @staticmethod
    def merge_arrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result_dict = {}

        for id, value in chain(nums1, nums2):
            if id in result_dict:
                result_dict[id] += value
            else:
                result_dict[id] = value

        return sorted(
            [[key, value] for key, value in result_dict.items()], key=lambda pair: pair[0]
        )

    @staticmethod
    def merge_arrays_1(
        nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        result = []

        nums1_iter = iter(nums1)
        nums2_iter = iter(nums2)

        n1 = next(nums1_iter, None)
        n2 = next(nums2_iter, None)

        while n1 is not None and n2 is not None:
            if n1[0] == n2[0]:
                result.append([n1[0], n1[1] + n2[1]])
                n1 = next(nums1_iter, None)
                n2 = next(nums2_iter, None)
            elif n1[0] > n2[0]:
                result.append(n2)
                n2 = next(nums2_iter, None)
            else:
                result.append(n1)
                n1 = next(nums1_iter, None)

        while n1 is not None:
            result.append(n1)
            n1 = next(nums1_iter, None)

        while n2 is not None:
            result.append(n2)
            n2 = next(nums2_iter, None)

        return result


if __name__ == "__main__":
    assert Solution().merge_arrays(
        nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]]
    ) == [[1, 6], [2, 3], [3, 2], [4, 6]]
    assert Solution().merge_arrays(
        nums1=[[2, 4], [3, 6], [5, 5]], nums2=[[1, 3], [4, 3]]
    ) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
