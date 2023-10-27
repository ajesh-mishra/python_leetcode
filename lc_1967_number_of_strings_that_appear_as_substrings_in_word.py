class Solution:
    @staticmethod
    def num_of_strings(patterns: list[str], word: str) -> int:
        return len([pattern for pattern in patterns if pattern in word])


if __name__ == "__main__":
    assert Solution().num_of_strings(patterns=["a", "abc", "bc", "d"], word="abc") == 3
    assert Solution().num_of_strings(patterns=["a", "b", "c"], word="aaaaabbbbb") == 2
    assert Solution().num_of_strings(patterns=["a", "a", "a"], word="ab") == 3
