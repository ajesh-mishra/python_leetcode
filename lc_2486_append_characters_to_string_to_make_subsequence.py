class Solution:
    @staticmethod
    def append_characters(s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j


if __name__ == "__main__":
    assert Solution.append_characters(s="coaching", t="coding") == 4
    assert Solution.append_characters(s="abcde", t="a") == 0
    assert Solution.append_characters(s="z", t="abcde") == 5
