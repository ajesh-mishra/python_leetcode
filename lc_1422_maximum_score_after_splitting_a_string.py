class Solution:
    @staticmethod
    def max_score(s: str) -> int:
        return max(
            [s[: i + 1].count("0") + s[i + 1 :].count("1") for i in range(len(s) - 1)]
        )



if __name__ == "__main__":
    assert Solution().max_score(s="011101") == 5
    assert Solution().max_score(s="00111") == 5
    assert Solution().max_score(s="1111") == 3
    assert Solution().max_score(s="00") == 1
