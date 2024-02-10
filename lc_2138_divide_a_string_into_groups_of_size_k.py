class Solution:
    def divide_string(self, s: str, k: int, fill: str) -> list[str]:
        start, end = 0, k
        result = []

        while end <= len(s):
            result.append(s[start:end])
            start = end
            end += k

        if reminder := len(s) % k:
            result.append(s[-reminder:] + (fill * (k - reminder)))

        return result
