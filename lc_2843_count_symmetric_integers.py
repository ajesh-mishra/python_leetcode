class Solution:
    def count_symmetric_integers(self, low: int, high: int) -> int:
        def is_symmetric(s: str) -> bool:
            if len(s) % 2 != 0:
                return False

            mid = len(s) // 2
            return sum([int(s) for s in s[:mid]]) == sum([int(s) for s in s[mid:]])

        return len([num for num in range(low, high + 1) if is_symmetric(str(num))])


if __name__ == "__main__":
    assert Solution().count_symmetric_integers(low=1, high=100) == 9
    assert Solution().count_symmetric_integers(low=1200, high=1230) == 4
    assert Solution().count_symmetric_integers(low=100, high=1782) == 44
