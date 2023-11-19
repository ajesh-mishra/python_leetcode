class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # reverse = lambda n: int(str(n)[::-1])
        # return num == reverse(reverse(num))

        s = str(num)
        if len(s) == 1:
            return True
        return not s.endswith("0")


if __name__ == "__main__":
    assert Solution().isSameAfterReversals(num=526)
    assert Solution().isSameAfterReversals(num=0)
    assert not Solution().isSameAfterReversals(num=1800)
