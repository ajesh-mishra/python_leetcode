class Solution:
    @staticmethod
    def can_be_equal(s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        new_s2 = s2[0] + s2[3] + s2[2] + s2[1]  # swap positions 1 and 3
        if s1 == new_s2:
            return True

        new_s2 = s2[2] + s2[1] + s2[0] + s2[3]  # swap positions 0 and 2
        if s1 == new_s2:
            return True

        new_s2 = s2[2] + s2[3] + s2[0] + s2[1]  # swap positions (1 and 3) and (0, 2)
        if s1 == new_s2:
            return True

        return False


if __name__ == "__main__":
    assert Solution().can_be_equal(s1="abcd", s2="cdab")
    assert not Solution().can_be_equal(s1="abcd", s2="dacb")
