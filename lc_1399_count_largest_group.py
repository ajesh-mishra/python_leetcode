class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n == 1:
            return 1

        def calculate_total(n: int) -> int:
            total = 0
            for num in str(n):
                total += int(num)
            return total

        map = {}

        for num in range(1, n + 1):
            total = calculate_total(num)
            if map.get(total):
                map[total] += 1
            else:
                map[total] = 1

        max_total = max(*map.values())
        return len(list(filter(lambda x: x == max_total, map.values())))


if __name__ == "__main__":
    # Solution().countLargestGroup(13)
    assert Solution().countLargestGroup(13) == 4
    assert Solution().countLargestGroup(2) == 2
