class Solution:
    @staticmethod
    def repeated_substring_pattern(s: str) -> bool:
        len_s = len(s)
        for i in range(1, (len_s // 2) + 1):
            if len_s % i != 0:
                continue
            if s[0:i] * (len_s // i) == s:
                return True

        return False

    @staticmethod
    def repeated_substring_pattern_1(s: str) -> bool:
        return any(
            [
                True
                for i in range(1, (len(s) // 2) + 1)
                if len(s) % i == 0 and s[0:i] * (len(s) // i) == s
            ]
        )


if __name__ == "__main__":
    assert Solution().repeated_substring_pattern("abab")
    assert Solution().repeated_substring_pattern("abcabcabcabc")
    assert not Solution().repeated_substring_pattern("aba")
