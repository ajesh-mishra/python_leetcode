class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        char_map = [0 for _ in range(26)]
        for word in words:
            for c in word:
                char_map[ord(c) - 97] += 1
        return all([count % len(words) == 0 for count in char_map])


if __name__ == "__main__":
    assert Solution().makeEqual(words=["abc", "aabc", "bc"])
    assert not Solution().makeEqual(words=["ab", "a"])
