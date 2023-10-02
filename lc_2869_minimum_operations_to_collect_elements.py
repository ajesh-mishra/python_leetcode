class Solution:
    def min_operations(self, nums: list[int], k: int) -> int:
        collection = set()
        for index, num in enumerate(nums[::-1]):
            if num > k:
                continue
            collection.add(num)
            if len(collection) == k:
                return index + 1


if __name__ == "__main__":
    assert Solution().min_operations(nums=[3, 1, 5, 4, 2], k=2) == 4
    assert Solution().min_operations(nums=[3, 1, 5, 4, 2], k=5) == 5
    assert Solution().min_operations(nums=[3, 2, 5, 3, 1], k=3) == 4
