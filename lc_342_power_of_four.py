class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(0, n):
            power = 4 ** i
            if power < n:
                continue
            elif power == n:
                return True
            else:
                return False


if __name__ == '__main__':
    assert Solution().isPowerOfFour(4)
    assert Solution().isPowerOfFour(64)
    assert Solution().isPowerOfFour(16)
    assert Solution().isPowerOfFour(1)
    assert not Solution().isPowerOfFour(5)
