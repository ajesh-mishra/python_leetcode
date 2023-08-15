class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))


if __name__ == '__main__':
    assert Solution().is_anagram(s='anagram', t='nagaram')
    assert not Solution().is_anagram(s='rat', t='car')
