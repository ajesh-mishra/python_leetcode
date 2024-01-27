class Solution:
    @staticmethod
    def nums_same_consecutive_diff(n: int, k: int) -> list[int]:
        def dfs(_n: int, _k: int, num: int) -> None:
            if _n == 0:
                result.append(num)
                return

            last_digit = num % 10

            if (next_digit := last_digit + _k) < 10:
                dfs(_n - 1, _k, 10 * num + next_digit)

            if (prev_digit := last_digit - _k) >= 0 and _k != 0:
                dfs(_n - 1, _k, 10 * num + prev_digit)

        result: list[int] = []

        for digit in range(1, 10):
            dfs(n - 1, k, digit)

        return result


if __name__ == "__main__":
    assert Solution().nums_same_consecutive_diff(n=3, k=7) == [181, 292, 707, 818, 929]
    assert Solution().nums_same_consecutive_diff(n=2, k=1) == [
        10,
        12,
        21,
        23,
        32,
        34,
        43,
        45,
        54,
        56,
        65,
        67,
        76,
        78,
        87,
        89,
        98,
    ]
