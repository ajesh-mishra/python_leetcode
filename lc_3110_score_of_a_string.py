class Solution:
    @staticmethod
    def score_of_string(s: str) -> int:
        return sum([abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)])


if __name__ == "__main__":
    assert Solution.score_of_string(s="hello") == 13
    assert Solution.score_of_string(s="zaz") == 50
