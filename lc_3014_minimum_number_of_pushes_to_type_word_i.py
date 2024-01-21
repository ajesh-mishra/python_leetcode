class Solution:
    def minimumPushes(self, word: str) -> int:
        q, r = len(word) // 8, len(word) % 8
        return sum([8 * i for i in range(q + 1)]) + r * (q + 1)


if __name__ == "__main__":
    assert Solution().minimumPushes()
