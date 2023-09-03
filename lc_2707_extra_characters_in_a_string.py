class Solution:
    @staticmethod
    def min_extra_char(s: str, dictionary: list[str]) -> int:
        end: int = len(s)
        words: set[str] = set(dictionary)
        cache: dict[int, int] = {end: 0}

        def dp(i: int) -> int:
            if i in cache:
                return cache[i]

            result = 1 + dp(i + 1)
            new_words = {word for word in words if word.startswith(s[i])}

            for j in range(i, end):
                if s[i : j + 1] in new_words:
                    result = min(result, dp(j + 1))

            cache[i] = result
            return result

        return dp(0)


if __name__ == "__main__":
    assert (
        Solution().min_extra_char(
            s="leetscode", dictionary=["leet", "code", "leetcode"]
        )
        == 1
    )
    assert (
        Solution().min_extra_char(s="sayhelloworld", dictionary=["hello", "world"]) == 3
    )
