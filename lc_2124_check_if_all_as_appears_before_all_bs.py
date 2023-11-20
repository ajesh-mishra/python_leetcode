class Solution:
    def check_string(self, s: str) -> bool:
        return s.rfind("a") < s.find("b") or s.find("b") == -1


if __name__ == "__main__":
    assert Solution().check_string(s="aaabbb")
    assert Solution().check_string(s="bbb")
    assert Solution().check_string(s="a")
    assert not Solution().check_string(s="abab")
