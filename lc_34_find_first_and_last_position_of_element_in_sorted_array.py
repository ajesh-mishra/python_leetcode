class Solution:
    @staticmethod
    def search_range(nums: list[int], target: int) -> list[int]:
        try:
            pos = nums.index(target)
        except ValueError:
            return [-1, -1]

        end = pos

        for i in range(pos, len(nums)):
            if nums[i] == target:
                end = i
                continue
            break

        return [pos, end]

    @staticmethod
    def search_range_1(nums: list[int], target: int) -> list[int]:
        def binary_search(start: int, end: int) -> int:
            if start >= end:
                if 0 <= start < len(nums) and nums[start] == target:
                    return start
                return -1

            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, end)
            else:
                return binary_search(start, mid - 1)

        result = binary_search(0, len(nums))

        if result == -1:
            return [-1, -1]

        start, end = result, result

        for i in range(start, -1, -1):
            if nums[i] == target:
                start = i
                continue
            break

        for i in range(end, len(nums)):
            if nums[i] == target:
                end = i
                continue
            break

        return [start, end]


if __name__ == "__main__":
    assert Solution().search_range(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert Solution().search_range(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert Solution().search_range(nums=[], target=0) == [-1, -1]
    assert Solution().search_range(nums=[1], target=1) == [0, 0]
    assert Solution().search_range(nums=[1, 3], target=1) == [0, 0]
    assert Solution().search_range(nums=[1], target=0) == [-1, -1]
    assert Solution().search_range(nums=[2, 2], target=3) == [-1, -1]
