class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        zero_list = [0 for _ in range(26)]

        for c in magazine:
            pos = ord(c) - 97
            if pos < 26:
                zero_list[pos] += 1

        for c in ransomNote:
            pos = ord(c) - 97
            if pos < 26:
                if zero_list[pos] == 0:
                    return False
                zero_list[pos] -= 1

        return True


if __name__ == "__main__":
    assert Solution().can_construct(ransomNote="aa", magazine="aab")
    assert not Solution().can_construct(ransomNote="a", magazine="b")
    assert not Solution().can_construct(ransomNote="aa", magazine="ab")
