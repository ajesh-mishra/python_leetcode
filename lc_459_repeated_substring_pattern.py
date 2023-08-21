class Solution:
    @staticmethod
    def repeated_substring_pattern(s: str) -> bool:
        len_s = len(s)
        for i in range(1, len_s):
            if len_s % i != 0:
                continue
            if s[0:i] * (len_s // i) == s:
                return True

        return False


if __name__ == '__main__':
    assert Solution().repeated_substring_pattern("abab")
    assert Solution().repeated_substring_pattern("abcabcabcabc")
    assert not Solution().repeated_substring_pattern("aba")
