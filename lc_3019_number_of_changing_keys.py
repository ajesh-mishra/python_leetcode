class Solution:
    def count_key_changes(self, s: str) -> int:
        return len([i for i in range(1, len(s)) if s[i].lower() != s[i - 1].lower()])


if __name__ == "__main__":
    assert Solution().count_key_changes(s="aAbBcC") == 2
    assert Solution().count_key_changes(s="AaAaAaaA") == 0
