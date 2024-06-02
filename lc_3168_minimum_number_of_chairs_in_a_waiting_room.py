class Solution:
    @staticmethod
    def minimum_chairs(s: str) -> int:
        count: int = 0
        max_count: int = 0

        for c in s:
            if c == "E":
                count += 1
                max_count = max(max_count, count)
            else:
                count -= 1

        return max_count
