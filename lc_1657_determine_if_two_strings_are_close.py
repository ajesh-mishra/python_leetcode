class Solution:
    def close_strings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_map = Solution.map(word1)
        word2_map = Solution.map(word2)

        for a, b in zip(word1_map, word2_map):
            if a == 0 and b == 0: continue
            if a != 0 and b != 0: continue
            return False

        if sorted(word1_map) != sorted(word2_map):
            return False

        return True

    @staticmethod
    def map(word):
        map_chars = [0 for _ in range(26)]
        for char in word:
            map_chars[ord(char) - 97] += 1

        return map_chars


if __name__ == "__main__":
    assert not Solution().close_strings(word1="abbzzca", word2="babzzcz")
    assert not Solution().close_strings(word1="uau", word2="ssx")
    assert Solution().close_strings(word1="abc", word2="bca")
    assert not Solution().close_strings(word1="a", word2="aa")
    assert Solution().close_strings(word1="cabbba", word2="abbccc")
