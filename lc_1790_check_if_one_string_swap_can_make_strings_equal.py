class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_mismatch: str | None = None
        second_mismatch: str | None = None

        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            if first_mismatch is None:
                first_mismatch = c1 + c2
                continue
            if second_mismatch is None:
                second_mismatch = c2 + c1
                if first_mismatch == second_mismatch:
                    continue
                return False
            return False

        return first_mismatch == second_mismatch


if __name__ == "__main__":
    assert Solution().areAlmostEqual(s1="bank", s2="kanb")
    assert Solution().areAlmostEqual(s1="kelb", s2="kelb")
    assert not Solution().areAlmostEqual(s1="attack", s2="defend")
